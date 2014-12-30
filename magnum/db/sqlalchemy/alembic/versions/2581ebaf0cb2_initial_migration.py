#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""initial migration

Revision ID: 2581ebaf0cb2
Revises: None
Create Date: 2014-01-17 12:14:07.754448

"""

# revision identifiers, used by Alembic.
revision = '2581ebaf0cb2'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # commands auto generated by Alembic - please adjust!
    op.create_table(
        'bay',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.Column('baymodel_id', sa.String(length=255), nullable=True),
        sa.Column('node_count', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    op.create_table(
        'baymodel',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.Column('type', sa.String(length=20), nullable=True),
        sa.Column('image_id', sa.String(length=255), nullable=True),
        sa.Column('flavor_id', sa.String(length=255), nullable=True),
        sa.Column('keypair_id', sa.String(length=255), nullable=True),
        sa.Column('external_network_id', sa.String(length=255), nullable=True),
        sa.Column('dns_nameserver', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    op.create_table(
        'container',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.Column('image_id', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    op.create_table(
        'node',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('type', sa.String(length=20), nullable=True),
        sa.Column('image_id', sa.String(length=255), nullable=True),
        sa.Column('ironic_node_id', sa.String(length=36), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    op.create_table(
        'pod',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.Column('desc', sa.String(length=255), nullable=True),
        sa.Column('bay_uuid', sa.String(length=36), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    op.create_table(
        'service',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.Column('bay_uuid', sa.String(length=36), nullable=True),
        sa.Column('labels', sa.Text, nullable=True),
        sa.Column('selector', sa.Text, nullable=True),
        sa.Column('ip', sa.String(length=36), nullable=True),
        sa.Column('port', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    # end Alembic commands


def downgrade():
    op.drop_table('bay')
    op.drop_table('baymodel')
    op.drop_table('container')
    op.drop_table('node')
    op.drop_table('service')
    op.drop_table('pod')
# We should probably remove the drops later ;-)
#    raise NotImplementedError(('Downgrade from initial migration is'
#                              ' unsupported.'))
