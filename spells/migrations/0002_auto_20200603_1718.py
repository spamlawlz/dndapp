# Generated by Django 3.0.7 on 2020-06-04 00:18

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spell',
            name='classes',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='index',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='material',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='saving_throw',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='subclasses',
        ),
        migrations.AddField(
            model_name='spell',
            name='area',
            field=models.CharField(blank=True, max_length=50, verbose_name='area of effect'),
        ),
        migrations.AddField(
            model_name='spell',
            name='attack_type',
            field=models.CharField(blank=True, choices=[('MELEE', 'a melee spell attack'), ('RANGED', 'a ranged spell attack')], max_length=6),
        ),
        migrations.AddField(
            model_name='spell',
            name='character_classes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('BARD', 'bard'), ('CLERIC', 'cleric'), ('DRUID', 'druid'), ('PALADIN', 'paladin'), ('RANGER', 'ranger'), ('SORCEROR', 'sorceror'), ('WARLOCK', 'warlock'), ('WIZARD', 'wizard')], default='WIZARD', max_length=56),
        ),
        migrations.AddField(
            model_name='spell',
            name='character_subclasses',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='spell',
            name='conditions',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('BLINDED', 'blinded'), ('CHARMED', 'charmed'), ('DEAFENED', 'deafened'), ('FRIGHTENED', 'frightened'), ('GRAPPLED', 'grappled'), ('INCAPACITATED', 'incapacitated'), ('INVISIBLE', 'invisible'), ('PARALYZED', 'paralyzed'), ('PETRIFIED', 'petrified'), ('POISONED', 'poisoned'), ('PRONE', 'prone'), ('RESTRAINED', 'restrained'), ('STUNNED', 'stunned'), ('UNCONSCIOUS', 'unconscious')], max_length=134),
        ),
        migrations.AddField(
            model_name='spell',
            name='damage_types',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('ACID', 'acid'), ('BLUDGEONING', 'bludgeoning'), ('COLD', 'cold'), ('FIRE', 'fire'), ('FORCE', 'force'), ('LIGHTNING', 'lightning'), ('NECROTIC', 'necrotic'), ('PIERCING', 'piercing'), ('POISON', 'poison'), ('PSYCHIC', 'psychic'), ('RADIANT', 'radiant'), ('SLASHING', 'slashing'), ('THUNDER', 'thunder')], max_length=100),
        ),
        migrations.AddField(
            model_name='spell',
            name='materials',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='spell',
            name='casting_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spell',
            name='components',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('V', 'verbal component'), ('S', 'somatic component'), ('M', 'material component')], max_length=3),
        ),
        migrations.AlterField(
            model_name='spell',
            name='desc',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='duration',
            field=models.CharField(max_length=100, verbose_name='spell duration'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='higher_level',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='level',
            field=models.IntegerField(choices=[(0, 'cantrip'), (1, 'first level'), (2, 'second level'), (3, 'third level'), (4, 'fourth level'), (5, 'fifth level'), (6, 'sixth level'), (7, 'seventh level'), (8, 'eighth level'), (9, 'ninth level')], verbose_name='spell level'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='spell name'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='school',
            field=models.CharField(choices=[('ABJURATION', 'abjuration'), ('CONJURATION', 'conjuration'), ('DIVINATION', 'divination'), ('ENCHANTMENT', 'enchantment'), ('EVOCATION', 'evocation'), ('ILLUSION', 'illusion'), ('NECROMANCY', 'necromancy'), ('TRANSMUTATION', 'transmutation')], max_length=20, verbose_name='school of magic'),
        ),
    ]
