from pathlib import Path
import re
from typing import Union
import PyPDF2


class PdfHandler:
    """excepts a Path or str to a pdf file and flags is true (contains sensitive data)
    or false (does not contain sensitive data)"""

    def __call__(self, path: Union[str, Path]) -> bool:
        file_obj = open(path, "rb")
        pdf_reader = PyPDF2.PdfReader(file_obj)

        head = " ".join(pdf_reader.pages[0].extract_text().split(" ")[:3])
        print(head)
        if head == "Financial Analysis Report":
            is_sensitive = False

        elif "arXiv" in head:
            is_sensitive = False

        else:
            # process first page
            try:
                first = pdf_reader.pages[0].annotations[0].get_object()["/V"]
                last = pdf_reader.pages[0].annotations[1].get_object()["/V"]
                street = pdf_reader.pages[0].annotations[2].get_object()["/V"]
                city = pdf_reader.pages[0].annotations[3].get_object()["/V"]
                country = pdf_reader.pages[0].annotations[4].get_object()["/V"]
                zipcode = pdf_reader.pages[0].annotations[5].get_object()["/V"]

                # print(first, last, street, city, country, zipcode)
            except Exception as e:
                # raise e
                pass

            # process second page
            try:
                text = pdf_reader.pages[1].extract_text()
                hits = {}
                text_items = text.split("\n")

                for i, item in enumerate(text_items[:-1]):
                    if item in [
                        "Company Name:",
                        "Type of Company:",
                        "Ownership Structure:",
                        "Date of Birth:",
                        "Name:",
                    ]:
                        hits[item] = text_items[i + 1]
                    if item in ["Client Information:"]:
                        hits[item] = text_items[i + 1 : i + 3]

                # print(hits)

                # detect sensitive data
                has_full_name = self.is_full_name(first, last)
                if not has_full_name:
                    if hits.get("Name:"):
                        name = hits["Name:"].split(" ")
                        if len(name) >= 2:
                            first = name[0]
                            last = name[1]
                        has_full_name = self.is_full_name(first, last)

                has_address = self.is_address(street, city, country, zipcode)

                if hits.get("Company Name:"):
                    has_company_name = self.is_company_name(hits.get("Company Name:"))
                else:
                    has_company_name = False

                if hits.get("Date of Birth:"):
                    has_dob = self.is_data_of_birth(hits.get("Date of Birth:"))
                else:
                    has_dob = False

                # flag true or false
                has_primary = int(has_full_name) + int(has_company_name)

                if has_primary >= 2:
                    is_sensitive = True
                elif has_primary == 1 and (has_dob or has_address):
                    is_sensitive = True
                else:
                    is_sensitive = False

                # print(is_sensitive)
                # print(first, last)
                # print("__")
                # print(has_full_name)
                # print(text)
                # print(has_address)
                # print(has_dob)

                # print(" ")

            except Exception as e:
                print(path)
                print(e)
                raise e

        return is_sensitive

    @staticmethod
    def is_data_of_birth(dob: str):
        if dob:
            dob_list = dob.split(" ")
            if len(dob_list) == 2:
                _, date_str = dob.split(" ")
                pattern = r"^\d{4}-\d{2}-\d{2}$"
                return bool(re.match(pattern, date_str))

            else:
                return False
        else:
            return False

    @staticmethod
    def is_company_name(company_name: str):
        if company_name:
            return True
        else:
            return False

    @staticmethod
    def is_address(street: str, city: str, country: str, zipcode: str):
        if street and city and country and zipcode:
            return True
        else:
            return False

    @staticmethod
    def is_full_name(first: str, last: str):
        if first and last:
            return True
        else:
            return False
