demo_dict = {"name":"sharda",
             "age":"25",
             "Location":"Mumbai"}
print(type(demo_dict))

demo_dict["age"]=23
print(demo_dict["age"])
print(demo_dict["Location"])
print(demo_dict)

# Remember   - key value should be unique.
print(type(demo_dict.keys()))
print(list(demo_dict.keys()))
