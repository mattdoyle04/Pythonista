import feedparser
import appex
import ui
import sys
if sys.version_info[0] >= 3:
	from urllib.request import urlretrieve
else:
	from urllib import urlretrieve
	
x,y = ui.get_screen_size()

def main():
	feed = feedparser.parse('http://feeds.bbci.co.uk/sport/rss.xml?edition=int')
	latest = feed['entries'][0]
	title = latest['title']
	description = latest['summary']

	alltext = title + '\n\n' + description
	
	label = ui.TextView()
	label.background_color = None
	label.editable = False
	label.text = alltext
	label.font = ('Arial',12)

	appex.set_widget_view(label)
	
if __name__ == '__main__':
	main()


