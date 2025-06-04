# demo_dict = {"name":"sharda",
#              "age":"25",
#              "Location":"Mumbai"}
# print(type(demo_dict))
#
# demo_dict["age"]=23
# print(demo_dict["age"])
# print(demo_dict["Location"])
# print(demo_dict)
#
# # Remember   - key value should be unique.
# print(type(demo_dict.keys()))
# print(list(demo_dict.keys()))

demo_dict ={"person1":{"name":"sharda",
                       "Age": 26,
                       "Location":"mumbai",
                        "courses":["python basics","API","selenium webdriver","Grid"]
                       },
            "person2": {"name":"tabli",
                        "Age": 24,
                        "Location":"Navi mumbai",
                        "courses":["python advance","API","selenium webdriver","Grid"]
                       },
            "key":"valueee"
            }
#print(list(demo_dict["person1"].values())[3][2])

# demo_dict.pop("person1")
# print(demo_dict)



# print(type(demo_dict))
# demo_dict["age"] = 25
# print(demo_dict)
# print(demo_dict["age"])

# print(demo_dict.keys())
# print((demo_dict.get("Location")))
# print(type(demo_dict.keys()))
# print(list(demo_dict.values())[0])
# print(list(demo_dict.items())[1])
# print(list(demo_dict.items())[1][0])
#
# Dict2 = demo_dict.copy()
# print(demo_dict)
# print(Dict2)

# x = (1,2,3,4,)
# y = (0)
# print(demo_dict)
# dict2= (demo_dict.fromkeys(x,y))
# print(demo_dict)
# print(type(dict2))
#dict2 = demo_dict.popitem()

print(demo_dict.update({"key":"aaa"}))
print(demo_dict)








