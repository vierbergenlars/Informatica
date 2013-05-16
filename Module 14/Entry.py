# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:17:11 2013

@author: lars
"""

class Entry(object):
     def __init__(self, day=1, description="Sleeping..."):
         self._day = day
         self._description = description
         self._slots = [0] * 24
     
     def get_description(self):
         return self._description
     
     def set_description(self, description):
         self._description = description
     
     def get_day(self):
         return self._day
                   
     def occupies_slot(self, slot):
        assert Entry.is_valid_slot(slot)
        return self._slots[slot-1] == 1
     
     @classmethod
     def is_valid_slot(cls,slot):
         return 1 <= slot <= 24;
         
     def overlaps_with(self, entry):
         return len(filter(lambda slot: entry.occupies_slot(slot+1), self._slots)) > 0
             
         
class MeetingEntry(Entry):
     
     def __init__(self, start = 0, end = 0, *args, **kwargs):
         super(self.__class__, self).__init__(*args, **kwargs)
         assert self.__class__.is_valid_slot(start, end)
         self._slots[start-1:end-1] = [1] * (end-start)
     
     def get_start_slot(self):
         return self._slots.index(1) + 1
     
     def get_end_slot(self):
         return abs(list(reversed(self._slots)).index(1)- len(self._slots)) + 1
         
     @classmethod
     def is_valid_slot(cls, start, end):
         return Entry.is_valid_slot(start) and Entry.is_valid_slot(end) and start < end
     
class PersonalEntry(Entry):
    def __init__(self, slots = set(), *args, **kwargs):
        super(self.__class__, self).__init__(*args,**kwargs)
        for slot in slots:
            self._slots[slot-1] = 1
    
    def add_slot(self, slot):
        assert self.__class__.is_valid_slot(slot)
        self._slots[slot-1] = 1
        
    def remove_slot(self, slot):
        assert self.__class__.is_valid_slot(slot)
        self._slots[slot-1] = 0
        
        


