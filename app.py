from flask import Flask, request, render_template
import aiosqlite
import asyncio

app = Flask(__name__)

db_file = messages_db.sqlite

@app.route('', methods=['GET', 'POST'])
async def index()
    query = request.form.get('query')
    results = []

    if query
        async with aiosqlite.connect(db_file) as connection
            async with connection.cursor() as cursor
                await cursor.execute(
                    SELECT chat_id, from_user_id, from_user_username, message_text FROM messages WHERE message_text LIKE ,
                    ('%' + query + '%',)
                )
                results = await cursor.fetchall()

    return render_template('index.html', results=results)

if __name__ == '__main__'
    app.run(debug=True)