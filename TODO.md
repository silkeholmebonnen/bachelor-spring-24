# To do

- [x] Merge branch med forskellige farve temaer
- [ ] Tilføj dokumentation for farver
- [ ] Få MoveAlongPathWithKilter til at virke for path's der krydser sig selv. Problemet er at vi nu bruger shapely's funktion `offset_curve` til at forskyde path'en, og denne virker ikke for path's der krydser (kun for path's der har areal 0)
- [ ] Implementer funktionalitet for at formindske/fortyde strømning.
