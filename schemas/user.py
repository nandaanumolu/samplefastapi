def userEntity(item) -> dict:
    print(item)
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "password":item["password"],
        "email":item["email"]
    }

def usersEntity(entity) ->list:
    return [userEntity(item) for item in entity]


def serializerDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},
            **{i:a[i] for i in a if i!="_id"}}

def serializerList(entity) ->list:
    return [serializerDict(a) for a in entity]
