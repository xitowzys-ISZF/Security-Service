migration-run:
	alembic revision --autogenerate -m 'initial'
	alembic upgrade head
