from packaging import version as pkg_version

with open('./version.txt', 'r') as fd:
        version = pkg_version.parse(fd.read())

with open('./version.txt', 'w') as fd:
    fd.write(f'{version.major}.{version.minor}.{version.micro + 1}\n')

print(f'{version} -> {version.major}.{version.minor}.{version.micro + 1}')
