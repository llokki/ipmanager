from logbook import Logger, FileHandler, StreamHandler
from app.models_def import IpAddresses, Networks
from app.validation import ip_validation, net_validation
from tortoise.contrib.pydantic import pydantic_model_creator
import sys

pydantic_ip = pydantic_model_creator(IpAddresses)
pydantic_net = pydantic_model_creator(Networks)

handler = FileHandler('../logs/ip_manager.log').push_application()
log = Logger('ip_manager')

#IP-address existence check

async def ip_check(ip):
        result = await pydantic_ip.from_queryset(IpAddresses.filter(ip = ip))
        if len(result) == 0:
            return False
        else:
            return True

async def net_check(net):
    result = await pydantic_net.from_queryset(Networks.filter(network = net ))
    if len(result) == 0:
        return False
    else:
        return True


#Viewing information about a single IP-address


async def ip_show(ip):
    if ip_validation(ip) is True:
        if await ip_check(ip) is True:
            message  = await pydantic_ip.from_queryset(IpAddresses.filter(ip = ip))
            result = {"message" : str(message), "status" : 200}
            return result
        else:
            message = {"IP-Address" : f"'{ip}' does not exist"}
            result = {"message" : message, "status" : 404}
            return result
    else:
        message = {"IP-Address" : f"'{ip}' is invalid"}
        result = {"message" : message, "status" : 400}
        return result



#This function remove ip address

async def ip_delete(ip):
    if ip_validation(ip) is True:
        if await ip_check(ip) is True:
            await IpAddresses.filter(ip = ip).delete()
            log.info(f'IP was delete -> {ip}')
            message = {"IP-address" : "Deleted"}
            result = {"message": message, "status": 200}
            return result
        else:
            log.warn(f'IP cannot be deleted -> Cause: {ip} does not exist')
            message = {"IP-address" : "Does not exist"}
            result = {"message": message, "status": 404}
            return result
    else:
        log.warn(f'IP cannot be deleted -> Cause: {ip} is invalid')
        message = {"IP-address": "Is invalid"}
        result = {"message": message, "status": 400}
        return result

#The following function allows you to change the IP-address and related data

async def ip_modify(ip, used, comment):
    if ip_validation(ip) is True:
        if await ip_check(ip) is True:
            if used == str('True'):
                answer = bool(True)
            else:
                answer = bool(False)
            await IpAddresses.filter(ip = ip).update(used = answer, comment = comment)
            log.info(f'IP was modify -> {ip}, {used}, {comment}')
            message = {"IP-Address": "Modification complete", "Look here": f"{ip},{used},{comment}"}
            result = {'message': message, 'status': 200}
            return result
        else:
            log.warn(f'IP cannot be modified -> Cause: {ip} does not exist')
            message = {"IP-Address": f"'{ip}' does not exist"}
            result = {'message': message, 'status': 404}
            return result
    else:
        log.warn(f'IP cannot be modified -> Cause: {ip} is invalid')
        message = {"IP-Address": f"'{ip}' is invalid"}
        result = {'message': message, 'status': 400}
        return result

#This function adds an entry to the IP address table

async def ip_add(ip, used, comment):
    if ip_validation(ip) is True:
        if await ip_check(ip) is False:
            if used == str('True'):
                answer = bool(True)
            else:
                answer = bool(False)
            await IpAddresses.create(ip=ip, used=answer, comment=comment)
            log.info(f'IP was modify -> {ip}, {used}, {comment}')
            message = {"IP-Address": "Successfully added", "Look here": f"{ip},{used},{comment}"}
            result = {'message': message, 'status': 200}
            return result
        else:
            log.warn(f'IP cannot be added -> Cause: {ip} is already exist')
            message = {"IP-Address": f"'{ip}' is already exist"}
            result = {'message': message, 'status': 412}
            return result
    else:
        log.warn(f'IP cannot be added -> Cause: {ip} is invalid')
        message = {"IP-Address": f"'{ip}' is invalid"}
        result = {'message': message, 'status': 400}
        return result

#Function to view the entire table

async def ip_view():
    return await pydantic_ip.from_queryset(IpAddresses.all())


async def net_show(net):
    if net_validation(net) is True:
        if await net_check(net) is True:
            message  = await pydantic_net.from_queryset(Networks.filter(network = net))
            result = {"message" : str(message), "status" : 200}
            return result
        else:
            message = {"Network" : f"'{net}' does not exist"}
            result = {"message" : message, "status" : 400}
            return result
    else:
        message = {"Network" : "Is incorrect, please try again"}
        result = {"message" : message, "status" : 400}
        return result



#This function remove ip address

async def net_delete(net):
    if net_validation(net) is True:
        if await net_check(net) is True:
            await Networks.filter(network = net).delete()
            log.info(f'Network was delete -> {net}')
            message = {"Network" : "Successfully deleted"}
            result = {"message": message, "status": 200}
            return result
        else:
            log.warn(f'Network cannot be deleted -> Cause: {net} does not exist')
            message = {"Network" : f"'{net}' does not exist"}
            result = {"message": message, "status": 412}
            return result
    else:
        log.warn(f'Network cannot be deleted -> Cause: {net} is invalid')
        message = {"Network": f"'{net}' is invalid"}
        result = {"message": message, "status": 400}
        return result

#The following function allows you to change the IP-address and related data

async def net_modify(net, active, comment):
    if net_validation(net) is True:
        if await net_check(net) is True:
            if active == str('True'):
                answer = bool(True)
            else:
                answer = bool(False)
            await Networks.filter(network = net).update(active = answer, comment = comment)
            log.info(f'Network was modify -> {net}, {active}, {comment}')
            message = {"Network": "Has been changed", "Look here": f"{net},{active},{comment}"}
            result = {'message': message, 'status': 200}
            return result
        else:
            log.warn(f'Network cannot be modified -> Cause: {net} does not exist')
            message = {"Network": f"'{net}' does not exist"}
            result = {'message': message, 'status': 404}
            return result
    else:
        log.warn(f'Network cannot be modified -> Cause: {net} is invalid')
        message = {"IP-Address": f"'{net}' is invalid"}
        result = {'message': message, 'status': 400}
        return result

#This function adds an entry to the IP address table

async def net_add(net, active, comment):
    if net_validation(net) is True:
        if await net_check(net) is False:
            if active == str('True'):
                answer = bool(True)
            else:
                answer = bool(False)
            await Networks.create(network = net, active = answer, comment = comment)
            log.info(f'New network was add -> {net}')
            message = {"Network": f"'{net}'Successfully added", "Look here": f"{net},{active},{comment}"}
            result = {'message': message, 'status': 200}
            return result
        else:
            log.warn(f'Network cannot be added -> Cause: {net} is already exist')
            message = {"Network": f"''{net}' is already exist"}
            result = {'message': message, 'status': 412}
            return result
    else:
        log.warn(f'Network cannot be added -> Cause: {net} is invalid')
        message = {"Network": f"'{net}' is invalid"}
        result = {'message': message, 'status': 400}
        return result

#Function to view the entire table

async def net_view():
    return await pydantic_net.from_queryset(Networks.all())
