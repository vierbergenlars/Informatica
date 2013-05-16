from Entry import *

#STEP 1
entry = Entry(description="Methodiek van de informatica")
assert entry.get_description() == "Methodiek van de informatica"

#STEP 2
entry = Entry(day=200)
assert entry.get_day() == 200

#STEP 3
meeting = MeetingEntry(description="Dinner",day=133,start=6,end=10)
assert meeting.get_description() == "Dinner"
assert meeting.get_day() == 133
assert meeting.get_start_slot() == 6
assert meeting.get_end_slot() == 10

#STEP 4
personal = PersonalEntry(description="Study",day=42,slots=frozenset([1,12,24]))
assert personal.get_description() == "Study"
assert personal.get_day() == 42
for slot in range(1,24):
  if (slot == 1) or (slot == 12) or (slot == 24):
    assert personal.occupies_slot(slot)
  else:
    assert not personal.occupies_slot(slot)
personal.add_slot(14)
for slot in range(1,24):
  if (slot == 1) or (slot == 12) or (slot == 14) or (slot == 24):
    assert personal.occupies_slot(slot)
  else:
    assert not personal.occupies_slot(slot)
personal.remove_slot(1)
personal.remove_slot(14)
personal.remove_slot(12)
personal.remove_slot(24)
for slot in range(1,24):
  if slot == 24:
    assert personal.occupies_slot(slot)
  else:
    assert not personal.occupies_slot(slot)

#STEP 5
meeting = MeetingEntry(description="Dinner",day=42,start=6,end=10)
personal = PersonalEntry(description="Study",day=42,slots=frozenset([1,7,23]))
assert meeting.overlaps_with(personal)
personal.remove_slot(7)
assert not personal.overlaps_with(meeting)
personal = PersonalEntry(description="Study",day=44,slots=frozenset([1,7,23]))
assert not meeting.overlaps_with(personal)
    
#STEP 6
meeting = MeetingEntry(description="Dinner",day=133,start=6,end=10)
assert not meeting.has_location() and (meeting.get_location() == None)
meeting.set_location("Leuven")
assert meeting.has_location() and (meeting.get_location() == "Leuven")
meeting.set_location(None)
assert not meeting.has_location() and (meeting.get_location() == None)

#STEP 7
meeting = MeetingEntry(description="Dinner",day=42,start=6,end=10)
personal = PersonalEntry(description="Study",day=53,slots=frozenset([1,7,23]))
assert meeting.starts_before(personal)
meeting = MeetingEntry(description="Dinner",day=66,start=6,end=10)
personal = PersonalEntry(description="Study",day=53,slots=frozenset([9,17,23]))
assert not meeting.starts_before(personal)
meeting = MeetingEntry(description="Dinner",day=42,start=6,end=10)
personal = PersonalEntry(description="Study",day=42,slots=frozenset([1,7,23]))
assert personal.starts_before(meeting)
assert not meeting.starts_before(personal)

