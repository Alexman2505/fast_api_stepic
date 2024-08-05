import uuid

# UUID1: основан на времени и MAC-адресе
uuid1 = uuid.uuid1()
print(f'UUID1: {uuid1}')

# UUID3: основан на MD5-хеше
uuid3 = uuid.uuid3(uuid.NAMESPACE_DNS, 'example.com')
print(f'UUID3: {uuid3}')

# UUID4: случайный UUID
uuid4 = uuid.uuid4()
print(f'UUID4: {uuid4}')

# UUID5: основан на SHA-1-хеше
uuid5 = uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com')
print(f'UUID5: {uuid5}')
