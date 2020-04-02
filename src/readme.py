import io
import os


config = {
    "repository_title": "Hackerrank Codes",
    "repository_name": "hackerrank-algo-ds",
    "repository_description": "My hackerrank codes for problem solving and algorithm implementation.",
    "profile_link": "https://hackerrank.com/ravgeetdhillon",
}


def get_file_name(file):
    file_name = os.path.splitext(file)[0]
    return file_name


def get_file_ext(file):
    file_ext = os.path.splitext(file)[1]
    return file_ext


def get_pretty_file_name(file):
    file_name = get_file_name(file)
    file_name = file_name.replace("_", " ")
    return file_name


def is_valid_code_file(file):
    file_name = get_file_name(file)
    file_ext = get_file_ext(file)
    if file_ext == ".py":
        return True
    return False


def get_files():
    valid_files = []
    for file in os.listdir("../"):
        if is_valid_code_file(file):
            file_data = {
                "pretty_name": get_pretty_file_name(file),
                "original_name": file
            }
            valid_files.append(file_data)
    return valid_files


def create_readme(codes):
    readme = io.open("../README.md", "w+")
    for line in io.open("readme.template", "r"):
        line = line.replace("$repository_title", config["repository_title"])
        line = line.replace("$repository_name", config["repository_name"])
        line = line.replace("$repository_description", config["repository_description"])
        line = line.replace("$profile_link", config["profile_link"])
        line = line.replace("$codes", codes)
        readme.write(line)
    readme.close()


def main():
    files = get_files()
    codes = ""
    for file in files:
        codes += "{} | [Link](https://github.com/ravgeetdhillon/{}/blob/master/{}) \n".format(file["pretty_name"], config["repository_name"], file["original_name"])

    create_readme(codes)


if __name__ == "__main__":
    main()
