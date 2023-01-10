class Solution(object):
    def sortSentence(self, s):

        temp= s.split()
        word={}
        coll=''
        for i in temp:
            word[i[-1]]= i[:-1]
        for i in sorted(word):
            coll=coll+''.join(word[i])+' '
        coll=coll[:-1]
        return coll
