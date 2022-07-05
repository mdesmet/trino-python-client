# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio

import trino.dbapi as dbapi


async def connect(*args, **kwargs):
    return Connection(*args, **kwargs)


class Connection:
    def __init__(self, *args, **kwargs):
        self.conn = dbapi.Connection(*args, **kwargs)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        loop = asyncio.get_running_loop()
        return loop.run_in_executor(None, lambda: self.conn.close())

    async def cursor(self, *args, **kwargs):
        return Cursor(self.conn.cursor(*args, **kwargs))


class Cursor:
    def __init__(self, cur: dbapi.Cursor):
        self.cur = cur

    async def execute(self, *args, **kwargs):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: self.cur.execute(*args, **kwargs))

    async def fetchone(self):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: self.cur.fetchone())

    async def fetchmany(self):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: self.cur.fetchmany())

    async def fetchall(self):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: self.cur.fetchall())
