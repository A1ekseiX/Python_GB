with open('nginx_logs.txt', encoding='utf=8') as file:
    result = []
    for el in file:
        remote_address = el.split(" ")[0]
        request_type = el.split(" ")[5]
        requested_resource = el.split(" ")[6]
        joining = remote_address, request_type, requested_resource
        result.append(joining)
print(*result, sep='\n')
