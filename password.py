from cryptography.fernet import Fernet

class PasswordManager:
    
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
        
    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)
    
    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()
    
    def create_password_file(self, path, initial_values=None):
        self.password_file = path
        # Write initial values to the password file if provided
        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)
    
    def load_password_file(self, path):
        self.password_file = path
        
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.strip().split(":")
                decrypted_password = Fernet(self.key).decrypt(encrypted.encode()).decode()
                self.password_dict[site] = decrypted_password
    
    def add_password(self, site, password):
        self.password_dict[site] = password
        
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + '\n')
    
    def get_password(self, site):
        try:
            return self.password_dict[site]
        except KeyError:
            return "Password not found for the specified site."
    
def main():
    password = {
        "email": "456789",
        "tiktok": "mytiktok123",
        "youtube": "casey123"
    }
    
    pm = PasswordManager()
    
    print("""
    (1) Create a new key.
    (2) Load an existing key.
    (3) Create new password file.
    (4) Load existing password file.
    (5) Add a new password.
    (6) Get a password.
    (q) Quit 
    """)
    
    done = False
    
    while not done:
        choice = input("Enter your choice: ")
        if choice == '1':
            path = input("Enter path for new key file: ")
            pm.create_key(path)
            print("New key created and saved.")
            
        elif choice == '2':
            path = input("Enter path for existing key file: ")
            pm.load_key(path)
            print("Key loaded successfully.")
            
        elif choice == '3':
            path = input("Enter path for new password file: ")
            pm.create_password_file(path, password)
            print("New password file created.")
            
        elif choice == '4':
            path = input("Enter path for existing password file: ")
            pm.load_password_file(path)
            print("Password file loaded successfully.")
        
        elif choice == '5':
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
            print(f"Password for {site} added.")
        
        elif choice == '6':
            site = input("What site do you want the password for? ")
            print(f"Password for {site}: {pm.get_password(site)}")
            
        elif choice == 'q':
            done = True
            print("Goodbye!")
        else:
            print("Invalid Choice!")
            
if __name__ == "__main__":
    main()
