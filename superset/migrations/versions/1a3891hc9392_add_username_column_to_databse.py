# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Adding extra field to Database model

Revision ID: 1a3891hc9392
Revises: fee7b758c130
Create Date: 2020-09-21 11:41:20.280841

"""
# revision identifiers, used by Alembic.
revision = "1a3891hc9392"
down_revision = "f9a30386bd74"

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column("dbs", sa.Column("database", sa.Text(), nullable=True))
    op.add_column("dbs", sa.Column("username", sa.Text(), nullable=True))
    op.add_column("dbs", sa.Column("host", sa.Text(), nullable=True))
    op.add_column("dbs", sa.Column("port", sa.Integer(), nullable=True))


def downgrade():
    op.drop_column("dbs", "database")
    op.drop_column("dbs", "username")
    op.drop_column("dbs", "host")
    op.drop_column("dbs", "port")