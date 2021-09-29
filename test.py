import requests
import xlsxwriter

def get_page(num):
    try:
        url = f'https://www.wongnai.com/_api/users/nickythedevil/photos.json?_v=6.042&locale=th&page.number={num}&page.size=1'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        response = requests.get(url, headers=headers)
        j_response = response.json()
        return j_response
        link = j_response.get('page').get('entities')[0].get('largeUrl')
        return link
    except:
        return False

def export_excel(num_continue):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('image_url_{num_continue}.xlsx')
    worksheet = workbook.add_worksheet()

    # Some data we want to write to the worksheet.
    list_cus = [
    ]
    for i in range(1, 20000):
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

num_continue = 101
print(get_page(101))

# export_excel(101)