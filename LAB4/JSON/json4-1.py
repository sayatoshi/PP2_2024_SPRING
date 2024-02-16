import json

file_path = "C:/Users/tumas/Desktop/Python/lab4/JSON/sample-data.json"

try:
    with open(file_path) as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: File 'sample-data.json' not found.")
    exit()

print("Interface Status")
print("="*80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-"*80)
for item in data['imdata']:
    l1_phys_if_attributes = item['l1PhysIf']['attributes']
    dn_value = l1_phys_if_attributes['dn']
    desc_value = l1_phys_if_attributes['descr']
    speed_value = l1_phys_if_attributes['speed']
    MTU_value = l1_phys_if_attributes['mtu']
    print("{:<50} {:<20} {:<8} {:<6}".format(dn_value, desc_value, speed_value, MTU_value))
