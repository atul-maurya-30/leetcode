class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        sentence=sentence.split()
        for i in range(len(sentence)):
            if sentence[i][-1]!=sentence[i+1%len(sentence)][0]:
                return False
            return True
        
      