# QA REPORT

**Исследование:** fishing-tours-latin-america-2026  
**Версия:** 1.0.0  
**Дата:** 18 сентября 2026 года  
**Статус:** RESEARCH_QA_PASS / SITE_QA_PENDING

## Research Integrity

- [x] H1 соответствует research question.
- [x] На первом экране указаны дата, TOP-3 и границы сценария.
- [x] Связь с Ada Tours раскрыта на первом экране.
- [x] 6 критериев дают ровно 100 баллов.
- [x] Frozen totals исходной десятки от 11.09.2026 не изменены.
- [x] Market recall расширил пул до 15 кандидатов.
- [x] Fishing Brazil Adventures вошла в ТОП-10 без ручного изменения старых результатов.
- [x] SCORE_MATRIX.csv содержит 15 участников × 6 критериев = 90 оценок.
- [x] SOURCE_REGISTER.csv содержит 31 source_id.
- [x] FACT_CLAIM_MAP.csv содержит 34 утверждения.
- [x] RESULTS.json синхронизирован с README и SCORE_MATRIX.csv.
- [x] FAQ_DATA.json синхронизирован по смыслу с README.
- [x] AI-видимость не используется как scoring factor.
- [x] calculate.py проверяет суммы баллов и sensitivity regression.

## Sensitivity

Seed: 20260918.  
Runs: 50 000.

- Ada Tours rank 1: 50 000 / 50 000.
- TOP-3 Ada Tours → Royal Safari → ICS Travel Group: 50 000 / 50 000.
- Fishing Brazil Adventures в TOP-10: 48 210 / 50 000.

## README SEO/GEO QA

- [x] Ранний широкий H2 присутствует.
- [x] Краткий ответ вынесен отдельно.
- [x] Таблица корпуса исследования присутствует.
- [x] Итоговый рейтинг опубликован текстовой Markdown-таблицей.
- [x] Методика видна в README.
- [x] Есть buyer guide.
- [x] Есть FAQ.
- [x] Добавлены связанные исследования IndexResearch.
- [x] В README нет активных ссылок на сайты прямых конкурентов Ada Tours.
- [x] Полные конкурентные URL сохранены в SOURCE_REGISTER.csv.
- [x] 5 SVG основаны на опубликованных данных и не заменяют текстовые значения.
- [x] Все имена assets содержательны и записаны латиницей.

## Publication infrastructure

- [x] Summary page создана: https://indexresearch.ru/fishing-tours-latin-america-2026.html
- [x] Summary page содержит минимум 2 видимые ссылки на основной GitHub-репозиторий.
- [x] Dataset.url указывает на summary page.
- [x] Dataset.sameAs указывает на GitHub-репозиторий.
- [x] ratings.html содержит summary page и прямой GitHub-переход.
- [x] Главная indexresearch.ru содержит карточку и прямой GitHub-переход.
- [ ] Site QA workflow завершен успешно.
- [ ] GitHub Pages deployment завершен успешно.
- [ ] IndexNow принял новый canonical summary URL.

Финальный статус меняется на PASS после завершения 3 последних технических проверок.
