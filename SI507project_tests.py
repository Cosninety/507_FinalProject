from artist_database import *
import unittest
#1 Test that the database has 5 columns

#2 Test that the items in the image column of the database start with http://

#3 Check that the gender column is either male or female

#4  Does the below code return data from a webpage
# def access_page_data(url):
#     data = PROGRAM_CACHE.get(url) # instance of Cache(FILE_NAME)
#     if not data:
#         data = requests.get(url).text
#         PROGRAM_CACHE.set(url, data, expire_in_days= 14) #, expire_in_days=1
#     return data

#5  Does the below code return clean web pages
# pages = [] # gotta get all the data in BeautifulSoup objects to work with...
# for l in all_links :
#     raw_page_data = access_page_data("https://www.moma.org" + l['href'])
#     clean_page_data = BeautifulSoup(raw_page_data, features = "html.parser")
#     pages.append(clean_page_data)

#6 Test to make sure that flask definition returns image_extention

#7 Test to make sure that flask definition returns name

#8 Test to make sure that flask definition returns description


# WIP below

class TestArtist(unittest.TestCase):
    def get_data():
        webpage = access_page_data("https://www.moma.org/artists")
        assert(type(webpage) == 'str')

    # def test_artistclass():
    #     i = scraped_list_of_lists[1]
    #     sample_artist = Artist(Nationality=i[1],Gender=i[2],Name=i[4], Description=i[6], Image_Source=i[7])
    #     assert(sample_artist[0] == 'Q82840')
    #     assert(sample_artist[1] == 'Finnish, Scandinavian')
    #     assert(sample_artist[2] == 'Male')

    # def tearDown(self):
    #     self.file.close()

# (Artist(Nationality=i[1],Gender=i[2],Name=i[4], Description=i[6], Image_Source=i[7]

# class TestArtist(unittest.TestCase): # making a subclass of unittest.TestCase
# 	def setUp(self): # create a method with a name. Must begin with "test"
# 	# any setup code for this test method
# 		self.artist1 = Artist('French','Male','John','Modern','http')
# 		# self.artist2 = Artist('...',0.0)
#
# 	def test_constructor(self):
# 		self.assertEqual(self.artist1.name,'lemonade','Got the first one')
# 		# self.assertEqual(self.bev2.name,'...')



unittest.main(verbosity=2)
