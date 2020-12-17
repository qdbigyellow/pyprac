import glob
import os
import concurrent.futures
import bs4
from bs4 import BeautifulSoup as bs

def read_xml(xml):
    with open(xml, 'r') as f:
        soup = bs(f, "xml")        
        print(os.path.basename(xml))
    return os.path.basename(xml)

def read_xml_w_bs(xml):
    with open(xml, 'r') as f:
        soup = bs(f, "xml")        
        for tag in soup.find_all('Tests'):
            print(f"tag name: {tag.name}")
            print(f"tag contents: {tag.contents}")
            print(f"tag string: {tag.string}")
            for n, v in tag.attrs.items():
                print(f"attribute - {n} : {v}")
            for child in tag.children:
                try:
                    print(f"child name {child.name}")
                    if isinstance(child, bs4.element.Tag):
                        print(f"child contents {child.contents}")
                    elif isinstance(child, bs4.element.NavigableString):
                        print(f"child string: {child}")

                except Exception as e:
                    print(f"Exception: {e}")
                    pass
    return None


if __name__ == '__main__':
    read_xml_w_bs(r'concurrent.futures\resources\Test1.xml')
    # when use multiprocessing, code must be guarded by __name__ == '__main__'
    # https://stackoverflow.com/questions/24374288/where-to-put-freeze-support-in-a-python-script
    # https://jizhi.im/blog/post/make_your_python_code_faster
    with concurrent.futures.ProcessPoolExecutor() as executor:
        xml_files = glob.glob(r"concurrent.futures\resources\*.xml")
        print(xml_files)
        for xml_file, thumbnai_file in zip(xml_files, executor.map(read_xml, xml_files)):
            print(f"{xml_file} is {thumbnai_file}")