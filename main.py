import json
from Contact import Contact
from Lead import Lead


def print_contacts():
    print("Contacts:")
    for contact in contactsList:
        print(contact.name, contact.email, contact.phone)


def print_leads():
    print("Leads:")
    for lead in leadsList:
        print(lead.name, lead.email, lead.phone)


def process_registrants(registrants):
    for jsonRegistrant in registrants:
        registrant = json.loads(str(jsonRegistrant))
        add_to_contacts = True
        check_leads = True
        for contact in contactsList:
            if registrant["email"] != "None":
                if registrant["email"] == contact.email:
                    print("Email Found in Contacts")
                    add_to_contacts = False
                    check_leads = False
                    if contact.phone == "None" and registrant["phone"] != "None":
                        contact.phone = registrant["phone"]
                    break
            if registrant["phone"] != "None":
                if registrant["phone"] == contact.phone:
                    print("Phone Found in Contacts")
                    add_to_contacts = False
                    check_leads = False
                    if contact.email == "None" and registrant["email"] != "None":
                        contact.email = registrant["email"]
                    break
        if check_leads:
            for lead in leadsList:
                if registrant["email"] != "None":
                    if registrant["email"] == lead.email:
                        print("Email Found in Leads")
                        add_to_contacts = False
                        if registrant["phone"] == "None":
                            registrant["phone"] = lead.phone
                        contactsList.append(Contact(registrant["name"], registrant["email"], registrant["phone"]))
                        leadsList.remove(lead)
                        break
                if registrant["phone"] != "None":
                    if registrant["phone"] == lead.phone:
                        print("Phone Found in Leads")
                        add_to_contacts = False
                        if registrant["email"] == "None":
                            registrant["email"] = lead.email
                        contactsList.append(Contact(registrant["name"], registrant["email"], registrant["phone"]))
                        leadsList.remove(lead)
                        break
        if add_to_contacts:
            contactsList.append(Contact(registrant["name"], registrant["email"], registrant["phone"]))


contactsList = []
leadsList = []
jsonRegistrantsList = {'{"name": "Lucy Liu", "email": "lucy@liu.com", "phone": "None"}',
                       '{"name": "Doug", "email": "doug@emmy.com", "phone": "4564445556"}',
                       '{"name": "Uma Thurman", "email": "uma@thurs.com", "phone": "None"}'}


contactsList.append(Contact("Alice Brown", "None", "1231112223"))
contactsList.append(Contact("Bob Crown", "bob@crowns.com", "None"))
contactsList.append(Contact("Carlos Drew", "carl@drewess.com", "3453334445"))
contactsList.append(Contact("Doug Emerty", "None", "4564445556"))
contactsList.append(Contact("Egan Fair", "eg@fairness.com", "5675556667"))

leadsList.append(Lead("None", "kevin@keith.com", "None"))
leadsList.append(Lead("Lucy", "lucy@liu.com", "3210001112"))
leadsList.append(Lead("Mary Middle", "mary@middle.com", "3331112223"))
leadsList.append(Lead("None", "None", "4442223334"))
leadsList.append(Lead("None", "ole@olson.com", "None"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Before Registrants")
    print_contacts()
    print_leads()
    print("")
    process_registrants(jsonRegistrantsList)
    print("After Registrants")
    print_contacts()
    print_leads()





