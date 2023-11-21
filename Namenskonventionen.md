# Namenskonventionen für REST-APIs

## Versionierung

Die Version einer REST-API sollte dem Semantic Versioning folgen.  
Das heißt es gibt eine dreistellige Versionsnummer, die durch Punkte getrennt wird.

Dabei wird in Major-, Minor- und Patch-Version unterschieden.

- Die **Major-Version** wird erhöht, wenn sich Breaking Changes ergeben.
- Die **Minor-Version** wird erhöht, wenn ein neues Feature hinzugefügt wurde, welches keine Breaking Changes verursacht.
- Die **Patch-Version** wird erhöht, wenn Bugfixes umgesetzt wurden.

## Namenskonventionen

In der URL sollte grundsätzlich der Plural für Objektnamen verwendet werden. Es sollte beispielsweise also immer `posts` und nicht `post` verwendet werden.

Diese Regel gilt auch, wenn ein einzelnes Objekt über seine ID aufgerufen wird.  
Sollte ein einzelnes Objekt aufgerufen werden, so wird die ID an die Objektnamen angehangen.

**Beispiel**

```
https://example.com/api/posts/<ID>
```

## Einsatz der HTTP-Methoden

| Method | Einsatz                                            |
|--------|----------------------------------------------------|
| GET    | Abrufen von Objekten                               |
| POST   | Hinzufügen von Objekten oder Triggern einer Aktion |
| PUT    | Ersetzen eines Objekts                             |
| PATCH  | Abändern eines Objekts                             |
| DELETE | Löschen eines Objekts                              |
