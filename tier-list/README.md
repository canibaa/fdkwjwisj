# 11th Grade Beauty Tier List

MVP интерфейса для закрытого голосования 11-й параллели.

## Архитектура

- GitHub Pages — frontend
- Supabase — база данных, Auth, Storage и серверные проверки
- Telegram bot — выдача одноразового приглашения и привязка Telegram user ID
- Cloudflare — защита/ограничение запросов
- Public results — только агрегированная статистика
- Admin — расширенная модерация и просмотр технических данных

## Режимы

1. Drag-and-drop Tier List: S/A/B/C/D.
2. Оценка по одной карточке.

## Следующий этап

- заменить demo participants на реальные данные;
- добавить Supabase schema + RLS;
- сделать Telegram bot;
- одноразовые invite tokens;
- защита от повторного голосования;
- публикация агрегированной статистики;
- admin dashboard;
- Cloudflare/rate limiting;
- подключить фотографии участников.
