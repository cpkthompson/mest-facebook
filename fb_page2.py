class FBPage:
    
    def __init__(self, page_type, page_name):
        self.page_type = page_type
        self.page_name = page_name


    def create_page(self):
        fbpage_category = ["advertising", "agriculture", "airport", "bussiness", "hotel", "hospital", "doctor"]
        print("Categories: {}".format(",".join(fbpage_category)))
            #join takes a list & prints it as a comma-separated string
        fbpage_type = ["local", "company", "brand", "artist", "entertainment", "community"]
            # .lower converts all Caps to lowercaps
        choice = input("Enter an page to create (Local, Company, Brand, Artist, Entertainment, Community): ")
        if choice.lower() in fbpage_type:
            page_name = input("Enter Page Name: ")
            page_type = input("Choose a Category: ")
            if page_type.lower() in fbpage_type:
                fbpage = FBPage(page_type, page_name)
                print("Creating FB {} Page for {}".format(page_type, page_name))
            else:
                print("No Such Category!!!")
        else:
            print("Invalid Choice!")

if if __name__ == '__main__':
    code()
    