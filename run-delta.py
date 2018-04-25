from subprocess import call

def main():
   list1 = ["abc", "def", "ghi"]
   list2 = ["abc2", "def2", "ghi2"]
   dict1 = {'path': list1, 'path2': list2}

   # takes a set, and concats into space seperated string
   files = ' '.join(str(path) for path in dict1.keys())
   multi = '~/commit-min/delta/multidelta'
   #call("", shell=True)
   print files

if __name__ == '__main__':
    main()

