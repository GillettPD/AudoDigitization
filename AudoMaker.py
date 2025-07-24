import json

# load entries already completed
with open("C:\\Users\\pdoug\\Documents\\Python_Projects\\Audo.json", 'r') as f:
    Audo = json.load(f)


# search numbered keys of top-level entries and find max to update new entries in-order
maxkey = 0
for key in Audo:
    thiskey = int(key)
    if thiskey > maxkey:
        maxkey = thiskey

# manually fill as many entries as desired w/ maxkey + 1, + 2 etc.

update = {
    str(maxkey + 1) : {
        'letter' : "ܐ",
        'letter_order' : '1',
        'heading' : "",
        'heading_root' : "",
        'definition' : "",
        'subheadings' : ""
    }
}

# update main dict
Audo.update(update)

# check for duplicate headings
rev = {}
for key, value in Audo.items():
    rev.setdefault(value['heading'], set()).add(key)

if [values for key, values in rev.items() if len(values) > 1]:
    raise Exception("Duplicate Entry")

# save to a json file
with open("C:\\Users\\pdoug\\Documents\\Python_Projects\\Audo.json", 'w') as f:
    json.dump(Audo, f)