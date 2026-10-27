# TRIZ skill for Claude

An Agent Skill that teaches Claude to solve stuck problems with **TRIZ**, the Theory of Inventive
Problem Solving (ТРИЗ, Теория решения изобретательских задач) by Genrich Altshuller.

TRIZ treats a hard problem as a **contradiction** (improving one thing makes another worse) and
resolves it instead of settling for a compromise. The skill works for engineering, software,
product, business and team problems, and for forecasting how a product will evolve.

[Русская версия ниже](#русский)

## What's inside

```
triz/
├── SKILL.md                    workflow: gate → model → contradictions → resources → evaluation
├── NOTICE.md                   data sources and attribution
├── references/
│   ├── principles.md           40 inventive principles, examples from 3 domains
│   ├── parameters.md           39 parameters with software and business equivalents
│   ├── problem-modeling.md     function model, operating zone, IFR, contradiction formulation
│   ├── separation.md           resolving physical contradictions
│   ├── resources.md            resource checklist
│   ├── su-field.md             su-field analysis and the 76 standards, condensed
│   ├── evolution.md            S-curve and trends of evolution
│   └── ariz.md                 ARIZ-85V, condensed working version
└── scripts/
    ├── matrix.py               contradiction matrix lookup (no dependencies)
    └── matrix.json             classical 39×39 matrix, verified
examples/                       scenarios and a worked example
evals/                          test prompts, including cases where TRIZ should NOT be used
```

## Design choices

- **The matrix is data, not memory.** Language models often misremember matrix cells, and
  several open-source TRIZ datasets turned out to be corrupted. This skill looks cells up with a
  script from a matrix checked against an independent source (see `triz/NOTICE.md`).
- **A gate before the method.** Ordinary bugs, comparisons and matters of taste are answered
  directly, without TRIZ.
- **No framework theater.** Claude reasons with TRIZ but answers with concrete mechanisms, risks
  and a next experiment. The TRIZ trail is shown only when the user asks for it.
- **Beyond engineering.** Parameters and principles come with software and business
  equivalents, so the classic matrix stays useful outside mechanics.
- **Progressive disclosure.** `SKILL.md` is short; reference files load only when a step needs them.

## Install

**Claude apps (claude.ai, desktop, mobile):** zip the `triz` folder (the folder itself, with
`SKILL.md` at its top level) and upload it as a custom skill in Claude's settings.

**Claude Code:** copy the folder into your skills directory:

```bash
git clone https://github.com/sampil/triz-skill.git
cp -r triz-skill/triz ~/.claude/skills/triz          # all projects
# or: cp -r triz-skill/triz .claude/skills/triz      # current project only
```

**Other agents** that read the Agent Skills format (`SKILL.md`) can use the same folder.

The lookup script needs Python 3.8+ and no packages:

```bash
python triz/scripts/matrix.py 14 1                        # improve strength, weight worsens
python triz/scripts/matrix.py --improve 9 39 --worsen 27 36
python triz/scripts/matrix.py --find latency
```

## Use

Describe the problem; the skill triggers on trade-offs and stuck problems. Or ask directly:
"use TRIZ", "find the contradiction", "run ARIZ on this", "where will this product go next?".
See [`examples/scenarios.md`](examples/scenarios.md) for ten scenarios across domains.

## Evaluate

[`evals/cases.json`](evals/cases.json) lists prompts and criteria. Run each prompt with and
without the skill and compare the answers blind. Include the negative cases: the skill should
stay out of them.

## License

MIT, see [LICENSE](LICENSE). Matrix data: see [triz/NOTICE.md](triz/NOTICE.md).

---

## Русский

Скилл для Claude, который решает «застрявшие» задачи с помощью **ТРИЗ** Генриха Альтшуллера:
находит противоречие (улучшаем одно, ухудшается другое) и разрешает его, а не ищет компромисс.
Подходит для техники, софта, продукта, бизнеса и команд, а также для прогноза развития продукта.

**Что внутри:** короткий алгоритм в `SKILL.md`, справочники по 40 приёмам (с примерами из трёх
областей), 39 параметрам (с «переводом» на софт и бизнес), принципам разрешения физических
противоречий, ресурсам, вепольному анализу и 76 стандартам, законам развития систем и сокращённому
АРИЗ-85В. Матрица Альтшуллера хранится как данные и читается скриптом, а не «по памяти».

**Как устроено:**
- сначала проверка, нужна ли вообще ТРИЗ (обычные баги и вопросы вкуса решаются напрямую);
- ТРИЗ остаётся «под капотом»: в ответе конкретные идеи, риски и следующий шаг; терминология
  только если пользователь сам просит разбор по ТРИЗ;
- ответ на языке пользователя.

**Установка:** заархивируйте папку `triz` в ZIP и загрузите как свой скилл в настройках Claude,
или скопируйте её в `~/.claude/skills/triz` для Claude Code.

**Примеры запросов:** «Помоги через ТРИЗ: …», «Найди противоречие в этой задаче»,
«Прогони это через АРИЗ», «Куда будет развиваться наш продукт по законам развития систем?».
Десять сценариев — в [`examples/scenarios.md`](examples/scenarios.md).
