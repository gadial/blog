---
id: 89
title: "עולמם המופלא של אליס ובוב"
date: 2007-11-17 10:24:20
layout: post
categories: 
  - קריפטולוגיה
---
הכירו את <a href="http://he.wikipedia.org/wiki/%D7%90%D7%9C%D7%99%D7%A1_%D7%95%D7%91%D7%95%D7%91">אליס ובוב</a>. הצמד הזה מככב בכל המחשה אפשרית לעניינים קריפטוגרפיים, ולעוד כמה עניינים אחרים, וגם אני לא אחמוק מהקונבנציה (ואפילו לא אעברת אותם ל"אסתר וברוך" או דבר מה דומה). הבעיה שלהם פשוטה: לאליס יש דבר מה שהיא רוצה להעביר לבוב בצורה בטוחה. הדרך הפשוטה ביותר לעשות זאת היא להביא לו אותו פיזית. בפועל, כאשר אליס ובוב מרוחקים, הם יזדקקו לשליח, ואז נשאלת השאלה האם אפשר לסמוך עליו. תוסיפו לכך את הסיכון הפעוט שמישהו יסתער על השליח, יתן לו בוקס ויחטוף את החפץ.

כל אלו הן בעיות בסיסיות גם בעולם המודרני בן זמננו, ובפרט באינטרנט. כל תקשורת אינטרנט מתבססת על הרבה "שליחים" שמעבירים את המידע ממחשב אחד לשני (בפרט, דרך ספק האינטרנט שלנו) ולא תמיד אפשר לסמוך עליהם; ותמיד קיימת סכנה שמישהו מצותת לקו שלנו, או אפילו משתלט עליו באופן זדוני.

אבל עזבו רגע אינטרנט. כיצד יפתרו אליס ובוב את בעיית העברת החפץ בעולם ה"אמיתי"? פתרון סביר הוא זה: אליס תיקח קופסה חסינת-כל (כלומר, לא ניתן לפתוח אותה בכוח הזרוע), תנעל אותה במנעול, ותשלח לבוב. לבוב יש את המפתח למנעול, ולכן הוא יכול לפתוח את התיבה ולהוציא את החפץ; לאף אחד מכוחות הזדון שבדרך אין את המפתח, כך שהתיבה חסרת ערך בשבילם. הם יוכלו אולי לקחת אותה ולהשליך אותה לנהר, אבל לחפץ הם לא יוכלו לעשות כלום. נשארנו רק עם בעיה אחת: לאליס צריך להיות מנעול, ולבוב צריך להיות מפתח למנעול. איך דבר שכזה יתבצע?

האפשרות הפשוטה יותר היא שאליס תפגוש את בוב יום אחד ושניהם ילכו לקנות מנעולים ומפתחות בצוותא. האפשרות השניה, המחוכמת מעט יותר, היא זו: בוב יקנה מבעוד מועד המוני עותקים זהים של מנעול קפיצי - כלומר, מנעול שניתן לנעול גם מבלי שיש לך את המפתח. את המפתח למנעולים הוא ישמור אצלו, ואילו את המנעולים הוא יפיץ בכל רחבי העולם - בפרט, ישלח כמה מהם לאליס. כעת, אם אליס רוצה לשלוח לבוב משהו, היא פשוט נועלת את התיבה במנעול שהוא שלח לה (ומרגע זה והלאה היא עצמה אינה מסוגלת לפתוח אותה - הרי אין לה את המפתח!) ושולחת לבוב.

היתרון שבשיטה זו הוא בכך שאליס ובוב לא צריכים לפגוש זה את זה כלל, אף פעם; מספיק שלאליס תהיה גישה לאחד מהמוני המנעולים שבוב הפיץ בעולם. גם בגישה זו יש סכנות - הנוכל הערמומי אוסקר (עוד שם שאני לא ממציא) עלול לשלוח לאליס מנעול שכתוב עליו "בוב", אבל למעשה אינו קשור כלל לבוב והמפתח שלו נמצא אצל אוסקר. לכן אליס תצטרך להשיג מנעולים של בוב ממקור שידוע שאפשר לבטוח עליו - נניח, ממשלת ארה"ב?

ברוכים הבאים לעולם המופלא של ה<a href="http://he.wikipedia.org/wiki/%D7%A7%D7%A8%D7%99%D7%A4%D7%98%D7%95%D7%92%D7%A8%D7%A4%D7%99%D7%94">קריפטוגרפיה</a>. בניגוד לתאורי הקופסאות והמנעולים שנתתי כאן, הצפנה עוסקת ב<strong>מידע</strong>. בפרט, בהקשר האינטרנטי שבו המושג כל כך רלוונטי בימינו, זהו מידע בינארי, שנתון כרצף של אפסים ואחדות, או בתור מספר טבעי גדול - פשוט כי כל מידע ממוחשב (מקובץ Word ועד לסרט AVI) אפשר לייצג כך.

מידע שכזה אי אפשר להכניס לקופסאות; אם שולחים אותו באינטרנט, חייבים להניח שכל מי שרק רוצה יוכל לקרוא (ולשנות!) את כל מה שאנחנו שולחים. לכן הקריפטוגרפיה עוסקת בדרכים <strong>לשנות</strong> את המידע הזה כך שיהיה חסר משמעות עבור מי שאין לו מידע נוסף שמסייע בפיענוח - ה"מפתח". שימושים מתקדמים קצת יותר של הקריפטוגרפיה מנסים להבטיח גם שלא ניתן יהיה לשנות את המידע, או להתחזות לשולח שלו, וכדומה.

פרט לקריפטוגרפיה, ישנה תורה אחרת שעוסקת בהעברה בטוחה של מידע - ה<a href="http://he.wikipedia.org/wiki/%D7%A1%D7%98%D7%92%D7%A0%D7%95%D7%92%D7%A8%D7%A4%D7%99%D7%94">סטגנוגרפיה</a>. בעוד שהקריפטוגרפיה מנסה לשנות את המידע, הסטגנוגרפיה מנסה להסתיר אותו - להחביא אותו בתוך מידע אחר, כך שיהיה קשה למצוא אותו, ואפילו בלתי אפשרי אם לא יודעים מה לחפש. דוגמה טריוויאלית מופיעה בספר "השד מהשביעית" - מבלי להרוס יותר מדי לקוראים העתידיים (הספר מאוד מומלץ!) אומר רק שאחת הדמויות מצליחה להחביא מסר בתוך מכתב תמים למראה על ידי שימוש באקרוסטיכון. דוגמאות מתוחכמות יותר בנות זמננו מתבססות, למשל, על שינוי הביט הפחות משמעותי בפיקסלים של תמונות (מה שבא לידי ביטוי בשינוי זניח ובלתי מורגש בגוון של נקודות בתמונה).

ההבדל בין קריפטוגרפיה וסטגנוגרפיה אינו חד וברור; עם זאת, לטעמי כלל אצבע טוב להפרדה הוא זה: אם הכרת ה<strong>שיטה</strong> ששימשה את המצפין הופכת את שחזור המידע למיידי, זוהי סטגנוגרפיה (כלומר, רק צריך לדעת "איפה להסתכל"). אם לא - כלומר, אם צריך מידע נוסף ("המפתח") כדי לשחזר - זוהי קריפטוגרפיה (וכמובן ששילוב של שתי השיטות רק מגדיל את הבטיחות). אכן, עקרון בסיסי בקריפטוגרפיה, שמצוטט חיש-קל בכל ספר בנושא, הוא "<a href="http://he.wikipedia.org/wiki/%D7%A2%D7%A7%D7%A8%D7%95%D7%9F_%D7%A7%D7%A8%D7%A7%D7%94%D7%95%D7%A4%D7%A1">עקרון קרקהופס</a>", הקובע כי שיטה קריפטוגרפית צריכה להיבחן תוך הנחה שכל המידע פרט למפתח ידוע.

כמובן שלא אמרתי כאן הרבה, כי לא ברור מה זה "מפתח"; במובן מסויים, המפתח הוא מכלול כל המרכיבים של מערכת ההצפנה שעשויים להשתנות בין הודעה להודעה, בזמן ש<strong>שיטת</strong> ההצפנה (אלגוריתם ההצפנה, אם תרצו) נותרת קבועה. יש הגיון בהפרדה הזו, שכן לרוב מבצעים מימוש יעיל לשיטת ההצפנה, עד כדי בניית חומרה מיוחדת שהיא אופטימלית עבורה, כך שהיא מרכיב קבוע יחסית של המערכת, בעוד שהמפתח משתנה שוב ושוב, ולרוב הוא פשוט רצף של ביטים.

מתבקשת דוגמה טריוויאלית להצפנה. דוגמה כזו היא "<a href="http://he.wikipedia.org/wiki/%D7%A6%D7%95%D7%A4%D7%9F_%D7%A7%D7%99%D7%A1%D7%A8">צופן קיסר</a>", שאומר בערך כך - יש לך הודעה שהיא רצף של אותיות? קח כל אות והזז אותה k מקומות קדימה בא"ב, כש-k (ה"היסט") הוא מספר טבעי כלשהו בין 1 ל-22 (במקרה של השפה העברית), ו"הזזה קדימה"היא ציקלית, כלומר א' מוזזת קדימה ב-4 מקומות זה ה', ואילו ש' מוזזת קדימה ב-4 מקומות זה ג' (לא לבלבל בין "הזזה קדימה" בא"ב, שעליה אני מדבר, ובין הזזת האותיות שבתוך המילה עצמה, שבה לא משתמשים).

k הוא המפתח הסודי, שבלעדיו לא ניתן לפענח את ההצפנה. ההודעה "תקפו עם שחר" הופכת עם מפתח של 3 ל-"גתרט קע בכא". שיחזור ההודעה המקורית מבוצע על ידי הזזת האותיות <strong>אחורה</strong> ב-3 מקומות. עבור <a href="http://he.wikipedia.org/wiki/%D7%99%D7%95%D7%9C%D7%99%D7%95%D7%A1_%D7%A7%D7%99%D7%A1%D7%A8">יוליוס קיסר</a> זה עבד (עם מפתח של 3), כנראה כי אז עוד לא שמעו על עיקרון קרקהופס; אם יודעים שנעשה שימוש בצופן קיסר צריך רק קצת סבלנות - יש 22 מפתחות אפשריים ולכן מנסים את כולם. מקבלים 22 הודעות מקוריות אפשריות; ככל הנראה רק אחת מהן תהיה בעלת משמעות, והרי לנו פיצוח. הלקח העיקרי כאן הוא שחייבים מספר גדול של מפתחות. גדול כל כך עד שיהיה קשה מאוד למפצח האפשרי לעבור על כולם, ולכן הוא ייצטרך לחפש "דרכי קיצור" - שגם אותן אסור לספק.

אם כן, שיטת קיסר כושלת, אבל יש לה הרחבה די פשוטה שהתגלתה כחזקה מאוד ונחשבה במשך שנים רבות ל"בלתי ניתנת לפיצוח" - <a href="http://he.wikipedia.org/wiki/%D7%A6%D7%95%D7%A4%D7%9F_%D7%95%D7%99%D7%96%27%D7%A0%D7%A8">צופן ויז'נר</a>. צופן ויז'נר זהה כמעט לחלוטין לקיסר, פרט לתעלול נוסף ומחוכם - לא מזיזים <strong>כל</strong> אות קדימה באותו היסט. במקום זה, בוחרים סדרה של כמה מספרים, ומזיזים באופן הבא: את האות הראשונה על פי המספר הראשון בסדרה, את השנייה על פי השני, וכן הלאה. כשנגמרת הסדרה, מתחילים מחדש (למשל, אם הסדרה היא בת 7 מספרים, אז את האות השמינית שוב מסיטים עם המספר הראשון שבה). <a href="http://he.wikipedia.org/wiki/%D7%A7%D7%95%D7%9E%D7%91%D7%99%D7%A0%D7%98%D7%95%D7%A8%D7%99%D7%A7%D7%94">קומבינטוריקה</a> פשוטה מראה שכאן מספר המפתחות הוא 22 בחזקת מספר האיברים שבסדרה - כלומר, כבר בסדרה בת 7 מספרים יש יותר משני מיליארד אפשרויות. בימים שלפני היות המחשב, מעבר על כל האפשרויות היה בלתי אפשרי.

עם הזמן התגלו טכניקות לפריצת השיטה הזו, שלא ניכנס אליהן עכשיו. מה השלב הבא? אם היסט בודד לא הספיק, ואם סדרה של היסטים באורך קבוע לא הספיקה, צריך לעבור לשלב הבא: היסט נפרד לכל אות בהודעה!

בואו נשכח לרגע מעברית ונחשוב על ההודעה שלנו בתור רצף של 0 ו-1. נניח שבתור מפתח הגרלנו רצף אחר של 0 ו-1, שבו כל תו יכול להיות או 0 או 1 בהסתברות אחידה. כעת אנו מחברים את המפתח עם ההודעה המקורית, עם כללי החיבור הרגילים פרט לכך שאחד ועוד אחד הוא אפס (זה מכונה "חיבור מודולו 2"). זו צורת ההצגה הפשוטה ביותר של מה שנקרא "<a href="http://he.wikipedia.org/wiki/%D7%A4%D7%A0%D7%A7%D7%A1_%D7%97%D7%93_%D7%A4%D7%A2%D7%9E%D7%99">צופן פנקס חד פעמי</a>" (One time pad), ואינו אלא הרחבה של צופן קיסר למצב שבו המפתח ארוך בדיוק כמו ההודעה שמצפינים. בניגוד לצופן קיסר ולצופן ויז'נר, הפנקס החד פעמי הוא <strong>בלתי ניתן לפיצוח</strong> - צופן מושלם. כפי ששמו מרמז, כדי שהצופן יהיה בלתי פציח, השימוש במפתח אכן חייב להיות חד פעמי - אם משתמשים באותו מפתח פעמיים, לא רק שהצופן הופך לניתן לפיצוח, זה אפילו לא קשה כל כך (המידע שהופך להיות זמין מיידית הוא ה-XOR של שתי ההודעות שהוצפנו, וזה כבר הרבה מאוד).

אפשר להתקומם נגד הטענה "בלתי ניתן לפיצוח". מבלי להיכנס ל<a href="http://he.wikipedia.org/wiki/%D7%A1%D7%95%D7%93%D7%99%D7%95%D7%AA_%D7%9E%D7%95%D7%A9%D7%9C%D7%9E%D7%AA">פורמליזם המתמטי</a> (שקיים, ומגדיר במדוייק את משמעות המושג הזה), הרעיון הוא כדלהלן. נניח ששאלתם אותי מה חיית המחמד שלי. עניתי "כגר", ואמרתי שזה מוצפן בפנקס חד פעמי. האם אתם יכולים לדעת מה החיה? אתם יודעים שזו מילה בת שלוש אותיות, אבל איזו? זה יכול להיות "כלב", או "זאב", או "שפן" או כל מילה אחרת בת שלוש אותיות (גם "עכג", השד יודע מה זה). כולן, <strong>בהסתברות שווה</strong>, עשויות להיות ההודעה המקורית שלי. בקיצור, אתם לא יכולים להפיק שום מידע מההודעה המוצפנת על המקור; אתם יכולים רק לנחש, וכל ניחוש שלכם טוב באותה המידה. אם רוצים להיות טהרנים ולהגיד שאפשר להפיק מידע מכך שזו מילה בת 3 אותיות, חשבו על זה כך: אני כותב את שם החיה, מוסיף הרבה סימני שאלה אחר כך (סימני שאלה ניתנים לקידוד במחשב, מן הסתם) עד שקיבלתי מילה שארוכה מכל מילה בעברית, ורק אז מצפין. עכשיו ברור שכל חיה שיש לה שם בעברית יכלה, בהסתברות שווה, להיות כתובה בהודעה שלי.

טוב, תשאלו, אם השיטה הזו באמת מושלמת, מה עוד יש לעשות בהצפנה? אי אפשר לסגור את העסק ולהשתמש רק בה?

התשובה היא, ראשית, שאכן - משתמשים בשיטה הזו לא מעט, כאשר סודיות מוחלטת היא הכרחית. אלא שיש לה מספר חסרונות בולטים, שאציין את שני העיקריים שבהם. הראשון הוא שכמות המפתח שצריך שווה לכמות המידע שרוצים להצפין: אם רוצים להצפין סרט וידאו של 700 מגה, צריך עוד 700 מגה של מפתח. כמובן, בימינו אין בעיה לקחת שליח עם מזוודה עמוסה בתקליטוני DVD עם מפתחות - חשבון פשוט מראה שחמש חבילות של 50 דיסקים, שבהחלט ניתן לסחוב במזוודה, מכילות יותר מטרה-בייט של מפתח. עם זאת, כאן אנו מגיעים לבעיה העיקרית - ההצפנה הזו היא מה שמכונה "הצפנה סימטרית", כלומר שני הצדדים צריכים לדעת את המפתח. זה אומר שצריך לשלוח את השליח עם מזוודת ה-DVD (בצורה מאובטחת, כמובן) לכל מקום שבו נמצא מישהו שרוצים לתקשר איתו. זה טוב ויפה כשאנחנו שירות ביון עם משאבים אדירים, אבל מה אם אנחנו אתר קניות צנוע באינטרנט?

חשבו על כך: באינטרנט, אתר קניות שלא מסוגל להציע אבטחה לא שווה כלום. לאתר קניות ממוצע יש - כמה, עשרות אלפי לקוחות? (נניח). עם כל לקוח כזה צריך לחלוק מפתח? איך אפשר לעשות את זה? הרי הלקוח לא ילך לאיזה סניף ויביא משם דיסקים עם מפתח וישתמש בהם; זה מסורבל ומעייף והוא יעבור לאתר אחר.

הפתרון לבעיה הזו הוא השימוש ב"מנעול הקפיץ" שתיארתי בהתחלה - שיטת הצפנה שבה מספיק שצד אחד ידע את המפתח, והצד השני ידע רק איך "לנעול". זה מתקשר לנושא הוצאות השורש שדיברתי עליו בפוסט הקודם: מתברר שהעלאה בריבוע היא "נעילה" שכזו, והוצאת שורש היא פתיחת מנעול שאפשרית רק למי שיודע את המפתח של פירוק n לשני גורמיו הראשוניים. שיטה שכזו (שבמקרה הספציפי הזה מכונה "<a href="http://he.wikipedia.org/wiki/%D7%94%D7%A6%D7%A4%D7%A0%D7%AA_%D7%A8%D7%91%D7%99%D7%9F">הצפנת רבין</a>", על שם <a href="http://he.wikipedia.org/wiki/%D7%9E%D7%99%D7%9B%D7%90%D7%9C_%D7%A8%D7%91%D7%99%D7%9F">מיכאל רבין</a>)  היא דוגמה פרטית של אחת התגליות החשובות ביותר במדעי המחשב מאז ומעולם - <a href="http://he.wikipedia.org/wiki/%D7%9E%D7%A4%D7%AA%D7%97_%D7%A6%D7%99%D7%91%D7%95%D7%A8%D7%99">הצפנת המפתח הציבורי</a>. ארחיב על כך בפעם הבאה.