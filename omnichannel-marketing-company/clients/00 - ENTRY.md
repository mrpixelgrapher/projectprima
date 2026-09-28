# clients

**Purpose:** the company's memory of each client. One folder per client, `clients/<client>/`, holds everything that outlives a single task: who they are, what they bought, their rates, their brief, voice, creator library, strategy, performance design, results, and every finished task. Every task for that client reads it; a retainer month starts from it.

| Folder | What it is |
|---|---|
| `00 - template/` | The empty client folder. `task.py new` copies it to `clients/<client>/` the first time a client appears |
| `<client>/` | One real (or rehearsal) client. The slug is the business noun from the request (`gemstone-seller`), never a person's name |

## Rules

- **Only gates write here** (`00 - control/01 - law/TASK_CONTRACT.md` §6). A gate copies a file its node produced and passed, or the client approved, into the client file its node ENTRY names. Nodes never edit client files mid-stage.
- **Nothing is lost.** Before a client file is replaced, the gate moves the old one to `<client>/versions/<file>-<YYYY-MM-DD>.md`.
- **Finished tasks live here.** `task.py` files every DONE or CLOSED task in `<client>/done/`. The client's whole history is in one place.
