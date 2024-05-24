from rest_framework import serializers
from .models import Technologies, Question, Choice

class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = ['id', 'title']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']

    def validate_choices(self, value):
        if len(value) != 4:
            raise serializers.ValidationError("Each question must have exactly 4 choices.")
        correct_choices = [choice for choice in value if choice['is_correct']]
        if len(correct_choices) != 1:
            raise serializers.ValidationError("Each question must have exactly one correct choice.")
        return value

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question

    def update(self, instance, validated_data):
        choices_data = validated_data.pop('choices')
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()

        # Update choices
        keep_choices = []
        for choice_data in choices_data:
            if 'id' in choice_data.keys():
                if Choice.objects.filter(id=choice_data['id']).exists():
                    c = Choice.objects.get(id=choice_data['id'])
                    c.choice_text = choice_data.get('choice_text', c.choice_text)
                    c.is_correct = choice_data.get('is_correct', c.is_correct)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = Choice.objects.create(question=instance, **choice_data)
                keep_choices.append(c.id)

        # Remove choices not included in the request
        for choice in instance.choices.all():
            if choice.id not in keep_choices:
                choice.delete()

        return instance
