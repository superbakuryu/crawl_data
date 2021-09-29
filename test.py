import requests
import xlsxwriter

# from random_user_agent.user_agent import UserAgent
# from random_user_agent.params import SoftwareName, OperatingSystem
# software_names = [SoftwareName.ANDROID.value]
# operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.MAC.value]   

# user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)

# # Get list of user agents.
# user_agents = user_agent_rotator.get_user_agents()

# user_agent_random = user_agent_rotator.get_random_user_agent()
# print(user_agent_random)

def recaptcha():
    url = 'https://www.wongnai.com/_gateway/recaptcha'
    response = requests.post(url)
    print(response.text)

def get_page(num):
    try:
        url = f'https://www.wongnai.com/_api/users/nickythedevil/photos.json?_v=6.042&locale=th&page.number={num}&page.size=1'
        # headers = {'User-Agent': user_agent_random}
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers=headers)
        j_response = response.json()
        # return j_response
        link = j_response.get('page').get('entities')[0].get('largeUrl')
        return link
    except:
        return False

def export_excel(num_continue):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(f'image_url_{num_continue}.xlsx')
    worksheet = workbook.add_worksheet()

    # Some data we want to write to the worksheet.
    list_cus = [
    ]
    for i in range(num_continue, 20000):
        print(i)
        link = get_page(i)
        lst = [link]
        list_cus.append(lst)
        if link == False:
            print("End at: ", i)
            break

    # Iterate over the data and write it out row by row.
    for row_num, data in enumerate(list_cus):
        worksheet.write_row(row_num, 0, data)

    workbook.close()
    print("Done")
    return True

num_continue = 140
print(get_page(num_continue))

# export_excel(num_continue)

# recaptcha()