def clean_name(name,upper=False):
    name=name.strip().title()
    name2=name.split()
    name=" ".join(name2)
    if (upper):
       name=name.upper()
    return(name )


print(clean_name("  maria jOHNSON "))
print(clean_name("  maria jOHNSON ", False))
print(clean_name("  maria jOHNSON ", True))
print(clean_name("ALBERT johnson"))
print(clean_name("ALBERT johnson", True))
print(clean_name("ALBERT   johnson"))
print(clean_name("ALBERT   johnson",True))
print(clean_name(""))
print(clean_name("   "))
print(clean_name("mary ann SMITH"))