import scanner


target_url = "https://www.tesla.com/"
links_to_ignore = ["https://www.tesla.com/teslaaccount/owner-xp/auth/logout?redirect=true&locale=en_US"]
data_dict = {"username": "dednanebe@gmail.com", "password": "Um_nn441", "Login": "submit"}


vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post("https://www.tesla.com/teslaaccount", data=data_dict)
vuln_scanner.crawl()
vuln_scanner.run_scanner()