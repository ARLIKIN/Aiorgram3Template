from fluent_compiler.bundle import FluentBundle

from fluentogram import FluentTranslator, TranslatorHub


def create_translator_hub() -> TranslatorHub:
    translator_hub = TranslatorHub(
        {
            "ru": ("ru", "en"),
        },
        [
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru-RU",
                    filenames=["bot/locales/ru/LC_MESSAGES/txt.ftl"]
                )
            ),
        ],
        root_locale='ru'
    )
    return translator_hub

# Todo: Для подсказок в коде
#  i18n -ftl bot/locales/ru/LC_MESSAGES/txt.ftl -stub bot/locales/stub.pyi
