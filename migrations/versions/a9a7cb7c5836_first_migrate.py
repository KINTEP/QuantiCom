"""First migrate

Revision ID: a9a7cb7c5836
Revises: 
Create Date: 2020-04-29 16:41:39.844388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9a7cb7c5836'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('mobile', sa.String(length=15), nullable=True),
    sa.Column('dstatus', sa.String(length=10), nullable=True),
    sa.Column('order_date', sa.DateTime(), nullable=True),
    sa.Column('ddate', sa.DateTime(), nullable=True),
    sa.Column('is_delivered', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_order_name'), ['name'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.Column('mobile', sa.String(length=12), nullable=True),
    sa.Column('regis_time', sa.DateTime(), nullable=False),
    sa.Column('online', sa.String(length=1), nullable=True),
    sa.Column('activation', sa.String(length=3), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('brand', sa.String(length=100), nullable=True),
    sa.Column('item', sa.String(length=100), nullable=True),
    sa.Column('product_code', sa.String(length=20), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_product_brand'), ['brand'], unique=False)
        batch_op.create_index(batch_op.f('ix_product_category'), ['category'], unique=False)
        batch_op.create_index(batch_op.f('ix_product_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_product_item'), ['item'], unique=False)
        batch_op.create_index(batch_op.f('ix_product_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_product_price'), ['price'], unique=False)
        batch_op.create_index(batch_op.f('ix_product_product_code'), ['product_code'], unique=False)

    op.create_table('search',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key_word', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('product', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('check_out',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer', sa.Integer(), nullable=False),
    sa.Column('product', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer'], ['user.id'], ),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('check_out', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_check_out_price'), ['price'], unique=False)

    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer', sa.Integer(), nullable=False),
    sa.Column('product', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer'], ['user.id'], ),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    with op.batch_alter_table('check_out', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_check_out_price'))

    op.drop_table('check_out')
    op.drop_table('cart')
    op.drop_table('search')
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_product_product_code'))
        batch_op.drop_index(batch_op.f('ix_product_price'))
        batch_op.drop_index(batch_op.f('ix_product_name'))
        batch_op.drop_index(batch_op.f('ix_product_item'))
        batch_op.drop_index(batch_op.f('ix_product_description'))
        batch_op.drop_index(batch_op.f('ix_product_category'))
        batch_op.drop_index(batch_op.f('ix_product_brand'))

    op.drop_table('product')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_order_name'))

    op.drop_table('order')
    # ### end Alembic commands ###