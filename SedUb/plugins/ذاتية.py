from SedUb import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from telethon import events
from telethon import types
from SedUb import *
Aljoker_Asbo3 = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}

@l313l.on(admin_cmd(pattern="(جلب الصورة|جلب الصوره|جلب الصوت|ذاتيه|ذاتية)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    
    lMl10l = await event.get_reply_message()
    
    if not lMl10l.media:
        return await event.edit("لا يمكن العثور على ملف قابل للتنزيل.")
    
    if not isinstance(lMl10l.media, (types.MessageMediaPhoto, types.MessageMediaDocument, types.MessageMediaVoice)):
        return await event.edit("يجب أن تكون الرسالة التي ترد عليها صورة أو صوت.")
    
    file = await lMl10l.download_media()
    
    await bot.send_file(
        "me",
        file=file,
        caption=f"""
- تـم حفظ الملف بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
- CH: @veevvw
- Dev: @Yll9ll
  """,
    )
    await event.delete()
#By @veevvw For You 🌹
@l313l.on(admin_cmd(pattern="(الذاتية تشغيل|ذاتية تشغيل)"))
async def reda(event):
    if gvarstatus ("savepicforme"):
        return await edit_delete(event, "**᯽︙حفظ الذاتيات مفعل وليس بحاجة للتفعيل مجدداً **")
    else:
        addgvar("savepicforme", "reda")
        await edit_delete(event, "**᯽︙تم تفعيل ميزة حفظ الذاتيات بنجاح ✓**")
 
@l313l.on(admin_cmd(pattern="(الذاتية تعطيل|ذاتية تعطيل)"))
async def Reda_Is_Here(event):
    if gvarstatus ("savepicforme"):
        delgvar("savepicforme")
        return await edit_delete(event, "**᯽︙تم تعطيل حفظ الذاتيات بنجاح ✓**")
    else:
        await edit_delete(event, "**᯽︙انت لم تفعل حفظ الذاتيات لتعطيلها!**")

def joker_unread_media(message):
    return message.media_unread and (message.photo or message.video or 
        (message.voice and getattr(message.media, 'ttl_seconds', 0) == 2147483647))

async def Hussein(event, caption):
    media = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    lMl10l_date = event.date.strftime("%Y-%m-%d")
    lMl10l_day = Aljoker_Asbo3[event.date.strftime("%A")]
    await bot.send_file(
        "me",
        media,
        caption=caption.format(sender.first_name, sender_id, lMl10l_date, lMl10l_day),
        parse_mode="markdown"
    )
    os.remove(media)

@l313l.on(events.NewMessage(func=lambda e: e.is_private and joker_unread_media(e) and e.sender_id != bot.uid))
async def Reda(event):
    if gvarstatus("savepicforme"):
        caption = """**
           ♡  غير مبري الذمة اذا استعملته للأبتزاز  ♡
♡ تم حفظ الذاتية بنجاح ✓
♡ تم الصنع : @veevvw
♡ أسم المرسل : [{0}](tg://user?id={1})
♡  تاريخ الذاتية : `{2}`
♡  أرسلت في يوم `{3}`
       ♡    ᥉᥆ᥙᖇᥴᥱ ᥉ᥱძƚɦ᥆ꪀ    ♡
        **"""
        await Hussein(event, caption)
