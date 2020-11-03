### N1 Kaffepause Kalender

Kildekode for N1 kaffepause kalendar som er hostet på https://marand.dk/n1-kaffepause-kalender/ lige nu.

##Indeholder apps

- generate_schedule: Genererer en kaffepause kalender (schedule.json) baseret på en liste af personer (persons.json)
- generate_frontend: Genererer en frontend baseret på kalenderen (schedule.json)
- send_mails: Sender en email til den person som skal stå for en kaffepause en given dag (ikke implementeret)

## Mulige forbedringer

- schedule_generator: uniform fordeling, så folk mødes med så mange som muligt / folk skal stå lige meget for kaffepauser. Det er bare tilfældigt lige nu.
- generate_frontend: centrer på nuværende dag
- generate_frontend: Pænere frontend + mobilvenlig
- send_mails: Implementer
- Måske en teams bot, som sender en besked til dem der skal stå for en kaffepause en given dag
- Måske er en gang om dagen for meget? Nu får vi se

Alle PRs er velkomne


