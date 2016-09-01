#!/usr/bin/python3
# coding=utf8

from bs4 import BeautifulSoup
html_doc = ""
with open("Cvpr2016.html") as f:
	html_doc = f.read()

soup = BeautifulSoup(html_doc, "lxml")

def write_to_file(sess_type="oral_sessions"):
	orals = soup.find_all("h3", id=sess_type)
	for oral in orals:
		subtitle = ""
		paper_title = ""
		paper_authors = ""
		for tag in oral.next_siblings:
			
			# get subtitle
			if tag.name == 'h4':
				subtitle = tag.string
			
			# get paper title and paper authors
			if tag.name == 'ul':
				paper_title_tag = tag.find('strong')
				paper_authors_tag = tag.find('p')

				if paper_title_tag and paper_authors_tag:
					paper_title = paper_title_tag.text.replace('\n', ' ')
					paper_authors = paper_authors_tag.text.replace('\n', ' ')
					# write to file
					with open(sess_type+" - "+subtitle+".txt", 'a') as f:
						f.write(paper_title)
						f.write('\n')
						f.write(paper_authors)
						f.write('\n\n')
				else:
					with open(sess_type+" - "+subtitle+".txt", 'a') as f:
						f.write("ERROR\n")
			if tag.name == 'hr':
				break


if __name__ == "__main__":
	sess = ["oral", "spotlight", "poster"]
	sess_id = [item + "_sessions" for item in sess]

	for id in sess_id:
		write_to_file(id)
		print("--------------done processing {}----------------".format(id))
