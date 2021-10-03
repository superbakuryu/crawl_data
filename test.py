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


def get_page(page_number, page_size):
    url = f'https://www.wongnai.com/_api/users/nickythedevil/photos.json?_v=6.042&locale=th&page.number={page_number}&page.size={page_size}'
    # headers = {'User-Agent': user_agent_random}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    print(response.text)


def export_excel():
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('image_url.xlsx')
    worksheet = workbook.add_worksheet()

    # Some data we want to write to the worksheet.
    list_cus = [
    ]
    for page_number in range(1, 101):
        try:
            url = f'https://www.wongnai.com/_api/users/nickythedevil/photos.json?_v=6.042&locale=th&page.number={page_number}&page.size=200'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            response = requests.get(url, headers=headers)
            j_response = response.json()
            # return j_response
            entities = j_response.get('page').get('entities')
            for i in range(len(entities)):
                index_of_excel = (page_number - 1)*200 + i
                print(index_of_excel)
                cus = [index_of_excel, entities[i].get('largeUrl')]
                list_cus.append(cus)
        except:
            print("End at: ", page_number)
            break
    # Iterate over the data and write it out row by row.
    for row_num, data in enumerate(list_cus):
        worksheet.write_row(row_num, 0, data)

    workbook.close()
    print("Done")
    return True


get_page(2000,1)
# export_excel()
