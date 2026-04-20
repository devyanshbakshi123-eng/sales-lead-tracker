leads = []

def add_lead():
    name = input("Enter client name: ")
    phone = input("Enter phone number: ")
    status = input("Enter status (New/Interested/Follow-up/Closed): ")
    
    lead = {
        "name": name,
        "phone": phone,
        "status": status
    }
    
    leads.append(lead)
    print("Lead added successfully!\n")

def view_leads():
    if not leads:
        print("No leads found.\n")
        return
    
    for i, lead in enumerate(leads):
        print(f"{i+1}. {lead['name']} - {lead['phone']} - {lead['status']}")
    print()

def main():
    while True:
        print("1. Add Lead")
        print("2. View Leads")
        print("3. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            add_lead()
        elif choice == "2":
            view_leads()
        elif choice == "3":
            break
        else:
            print("Invalid choice\n")

main()
