# Generated by Django 5.1.4 on 2024-12-06 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("country", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("street", models.CharField(max_length=100)),
                ("house_number", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
                ("release_date", models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name="networknode",
            name="city",
        ),
        migrations.RemoveField(
            model_name="networknode",
            name="country",
        ),
        migrations.RemoveField(
            model_name="networknode",
            name="email",
        ),
        migrations.RemoveField(
            model_name="networknode",
            name="house_number",
        ),
        migrations.RemoveField(
            model_name="networknode",
            name="product_model",
        ),
        migrations.RemoveField(
            model_name="networknode",
            name="product_name",
        ),
        migrations.RemoveField(
            model_name="networknode",
            name="product_release_date",
        ),
        migrations.RemoveField(
            model_name="networknode",
            name="street",
        ),
        migrations.AlterField(
            model_name="networknode",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="networknode",
            name="debt",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="networknode",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="networknode",
            name="supplier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="network.networknode",
            ),
        ),
        migrations.AddField(
            model_name="networknode",
            name="contact",
            field=models.OneToOneField(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="network.contact",
            ),
        ),
        migrations.AddField(
            model_name="networknode",
            name="products",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="network.product",
            ),
        ),
    ]
