import os
import re
import pandas as pd

class Extractor():
  def __init__(self, text):
    self.text = text
      
  def direct_speech(self):  
    paragraphs = self.text.split('\n')
    all_paragraphs = []
    for para in paragraphs:
      paragraph = '\n' + para +'\n'
      all_paragraphs.append(paragraph)
      
    dialogue = []
    for paragraph in all_paragraphs:
      huge_replica_1 = re.findall('\n *[–|-] *[А-Я].*?\n|\n *[–|-] *[A-Z].*?\n', paragraph)
      if len(huge_replica_1) != 0:
        for hugereplica in huge_replica_1:
          replicas_and_authors_1_2 = re.findall('[–|-][–|-].*?[(!)+|(?)+|.|,|...|…|..|!?|?!|?!?|!?!|!..|?..](?= *[–|-][–|-].*?[(!)+|(?)+|.|...|…|..|,|!?|?!|?!?|!?!|!..|?..])', hugereplica)
          if len(replicas_and_authors_1_2) != 0:
            for index in range(len(replicas_and_authors_1_2)):
              if index % 2 == 0:
                dialogue.append(replicas_and_authors_1_2[index])
            if len(replicas_and_authors_1_2) % 2 == 0:
              last_extracted = replicas_and_authors_1_2[len(replicas_and_authors_1_2)-1]
              last_extracted = last_extracted.replace('.','\.').replace('?','\?').replace('*','\*').replace('+','\+').replace('(','\(').replace(')','\)').replace('[','\[').replace(']','\]')
              last_replica = re.findall('(?<={last_extracted}).*'.format(last_extracted = last_extracted), hugereplica)
              dialogue = dialogue + last_replica
          # replicas starting with –        
          else:
            replicas_and_authors_1 = re.findall('–.*?[(!)+|(?)+|.|,|...|…|..|!?|?!|?!?|!?!|!..|?..](?= *–.*?[(!)+|(?)+|.|...|…|..|,|!?|?!|?!?|!?!|!..|?..])', hugereplica)
            if len(replicas_and_authors_1) != 0:
              for index in range(len(replicas_and_authors_1)):
                if index % 2 == 0:
                  dialogue.append(replicas_and_authors_1[index])
              if len(replicas_and_authors_1) % 2 == 0:
                last_extracted = replicas_and_authors_1[len(replicas_and_authors_1)-1]
                last_extracted = last_extracted.replace('.','\.').replace('?','\?').replace('*','\*').replace('+','\+').replace('(','\(').replace(')','\)').replace('[','\[').replace(']','\]')
                last_replica = re.findall('(?<={last_extracted}).*'.format(last_extracted = last_extracted), hugereplica)
                dialogue = dialogue + last_replica
            else:
              replicas_and_authors_1_1 = re.findall('-.*?[(!)+|(?)+|.|,|...|…|..|!?|?!|?!?|!?!|!..|?..](?= *-.*?[(!)+|(?)+|.|...|…|..|,|!?|?!|?!?|!?!|!..|?..])', paragraph)
              if len(replicas_and_authors_1_1) != 0:
                for index in range(len(replicas_and_authors_1_1)):
                  if index % 2 == 0:
                    dialogue.append(replicas_and_authors_1_1[index])
                if len(replicas_and_authors_1_1) % 2 == 0:
                  last_extracted = replicas_and_authors_1_1[len(replicas_and_authors_1_1)-1]
                  last_extracted = last_extracted.replace('.','\.').replace('?','\?').replace('*','\*').replace('+','\+').replace('(','\(').replace(')','\)').replace('[','\[').replace(']','\]')
                  last_replica = re.findall('(?<={last_extracted}).*'.format(last_extracted = last_extracted), hugereplica)
                  dialogue = dialogue + last_replica
              else:
                for replica in huge_replica_1:
                  dialogue.append(replica.replace('\n', ''))
      # replicas starting with «»
      else:
        # «Direct speech» - author's comment
        short_replica_1 = re.findall('[«|\"|\'].*?[а-я].*?[»|\"|\'](?= *[–|-])', paragraph)
        if len(short_replica_1) != 0:
          dialogue = dialogue + short_replica_1
        # author's comment: «Direct speech»
        short_replica_2 = re.findall('(?<=:) *[«|\"|\'].*?[»|\"|\']', paragraph)
        if len(short_replica_2) != 0:
          for rep in short_replica_2:
            if rep not in short_replica_1:
              dialogue.append(rep)
        huge_replica_2 = re.findall('[«|\"|\'].*?[(!)+|(?)+|.|,|...|…|..|!?|?!|?!?|!?!|!..|?..] *[–|-][–|-].*?[»|\"|\']', paragraph)
        if len(huge_replica_2) != 0:
          for sentence in huge_replica_2:
            replicas_and_authors_2 = re.findall('.*?[(!)+|(?)+|.|,|...|…|..|!?|?!|?!?|!?!|!..|?..] *(?=[–|-][–|-])', sentence)
            if len(replicas_and_authors_2) != 0:
              for index in range(len(replicas_and_authors_2)):
                if index % 2 == 0:
                  if replicas_and_authors_2[index] not in short_replica_1 and replicas_and_authors_2[index] not in short_replica_2:
                    dialogue.append(replicas_and_authors_2[index])
              if len(replicas_and_authors_2) % 2 == 0:
                last_extracted_2 = replicas_and_authors_2[len(replicas_and_authors_2)-1]
                last_extracted_2 = last_extracted_2.replace('.','\.').replace('?','\?').replace('*','\*').replace('+','\+').replace('(','\(').replace(')','\)').replace('[','\[').replace(']','\]')
                last_replica_2 = re.findall('(?<={last_extracted_2}).*'.format(last_extracted_2 = last_extracted_2), sentence)
                for i in last_replica_2:
                  if i not in short_replica_1 and i not in short_replica_2:
                    dialogue.append(i)
        else:
          huge_replica_2_1 = re.findall('[«|\"|\'].*?[(!)+|(?)+|.|,|...|…|..|!?|?!|?!?|!?!|!..|?..] *–.*?[»|\"|\']', paragraph)
          if len(huge_replica_2_1) != 0:
            for sentence in huge_replica_2_1:
              replicas_and_authors_2 = re.findall('.*?[(!)+|(?)+|.|,|...|…|..|!?|?!|?!?|!?!|!..|?..] *(?=–)', sentence)
              if len(replicas_and_authors_2) != 0:
                for index in range(len(replicas_and_authors_2)):
                  if index % 2 == 0:
                    if replicas_and_authors_2[index] not in short_replica_1 and replicas_and_authors_2[index] not in short_replica_2:
                      dialogue.append(replicas_and_authors_2[index])
                if len(replicas_and_authors_2) % 2 == 0:
                  last_extracted_2 = replicas_and_authors_2[len(replicas_and_authors_2)-1]
                  last_extracted_2 = last_extracted_2.replace('.','\.').replace('?','\?').replace('*','\*').replace('+','\+').replace('(','\(').replace(')','\)').replace('[','\[').replace(']','\]')
                  last_replica_2 = re.findall('(?<={last_extracted_2}).*'.format(last_extracted_2 = last_extracted_2), sentence)
                  for i in last_replica_2:
                    if i not in short_replica_1 and i not in short_replica_2:
                      dialogue.append(i)
          else:
            huge_replica_2_2 = re.findall('[«|\"|\'].*?[(!)+|(?)+|.|,|...|…|..|!?|?!|?!?|!?!|!..|?..] *-.*?[»|\"|\']', paragraph)
            if len(huge_replica_2_2) != 0:
              for sentence in huge_replica_2_2:
                replicas_and_authors_2 = re.findall('.*?[(!)+|(?)+|.|,|...|…|..|!?|?!|?!?|!?!|!..|?..] *(?=-)', sentence)
                if len(replicas_and_authors_2) != 0:
                  for index in range(len(replicas_and_authors_2)):
                    if index % 2 == 0:
                      if replicas_and_authors_2[index] not in short_replica_1 and replicas_and_authors_2[index] not in short_replica_2:
                        dialogue.append(replicas_and_authors_2[index])
                  if len(replicas_and_authors_2) % 2 == 0:
                    last_extracted_2 = replicas_and_authors_2[len(replicas_and_authors_2)-1]
                    last_extracted_2 = last_extracted_2.replace('.','\.').replace('?','\?').replace('*','\*').replace('+','\+').replace('(','\(').replace(')','\)').replace('[','\[').replace(']','\]')
                    last_replica_2 = re.findall('(?<={last_extracted_2}).*'.format(last_extracted_2 = last_extracted_2), sentence)
                    for i in last_replica_2:
                      if i not in short_replica_1 and i not in short_replica_2:
                        dialogue.append(i)
            else:
              if len(short_replica_1) == 0 and len(short_replica_2) == 0:
                huge_replica_3 = re.findall('\n *[«|\"|\'].*?[»|\"|\'] *\n', paragraph)
                if len(huge_replica_3) != 0:
                  for replica in huge_replica_3:
                    dialogue.append(replica.replace('\n', ''))
    return dialogue

  def statistics(self, dialogue):  
    # book wordcount
    book_words = len(re.findall(r'\w+', self.text))
    all_dialogues = ' '.join(dialogue)
    dialogue_words = len(re.findall(r'\w+', all_dialogues))
    ratio = dialogue_words/book_words
    statisctics_dict = {'text_wordcount': book_words, 'direct_speech_wordcount': dialogue_words, 'ratio': ratio}
    return statisctics_dict
