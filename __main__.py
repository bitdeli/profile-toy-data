from bitdeli import profile_events

for profile, events in profile_events():
    profile.setdefault('events', []).extend(e.object for e in events)
