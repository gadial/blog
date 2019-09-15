---
id: 137
title: "מסיבת יום הולדת לביצה - הפתרונות"
date: 2008-07-05 17:20:01
layout: post
categories: 
  - משחקים וחידות מתמטיות
---
ב<a href="http://www.gadial.net/?p=136">פוסט הקודם</a> הצגתי מספר חידות, וכעת אנסה להציג פתרונות אפשריים עבורן - בשום פנים ואופן איני טוען שאלו הפתרונות היחידים. נתחיל מ<a href="http://he.wikipedia.org/wiki/%D7%A4%D7%A8%D7%93%D7%95%D7%A7%D7%A1_%D7%99%D7%95%D7%9D_%D7%94%D7%94%D7%95%D7%9C%D7%93%D7%AA">פרדוקס יום ההולדת</a>. התשובה המספרית היא 23 - אם יש לפחות כמספר הזה של אנשים במסיבה, יש הסתברות גבוהה מחצי (בהינתן שימי ההולדת שלהם מתפלגים באופן אחיד) שלשניים יהיה אותו יום הולדת. לדעתי זוהי תוצאה מפתיעה למדי, כי האינטואיציה שלי אומרת לי שכדי לקבל הסתברות של 1/2 צריך בערך 1/2 ממספר האנשים שנדרשים כדי לקבל הסתברות של 1, דהיינו חצי מ-366, דהיינו בערך 180; אבל כמובן שהאינטואיציה שלי היא חסרת כל ביסוס, ולא רק במקרה הספציפי של הפרדוקס הזה.

לא אכנס כרגע להוכחה ש-23 אכן מקיים את התכונה המבוקשת; תחת זאת, אקדיש בהמשך פוסט שלם לפרדוקס החביב הזה.

נעבור לעניין המסיבה והחברים/אויבים. להוכיח שבכל שישיה, או שיש שלשה שכולם חברים, או שיש שלשה שכולם בה אויבים זה יחסית קל. בוחרים אדם אחד מהשישיה - נקרא לו בשם המקורי "אדם". כעת נטענת הטענה הפשוטה הבאה: או שמבין שאר חברי השישיה יש לאדם לפחות שלושה חברים, או שיש לו לפחות שלושה אויבים. מדוע? כי כל אחד מחמשת האנשים  האחרים שבשישיה הוא או אויב של אדם או חבר שלו, ואם היינו מגבילים את מספר החברים והאויבים של אדם להיות שניים מכל סוג, היינו "מכסים" בכך רק ארבעה אנשים. זו המחשה נאה לאבחנה מתמטית בסיסית ושימושית - "<a href="http://he.wikipedia.org/wiki/%D7%A2%D7%A7%D7%A8%D7%95%D7%9F_%D7%A9%D7%95%D7%91%D7%9A_%D7%94%D7%99%D7%95%D7%A0%D7%99%D7%9D">עקרון שובך היונים</a>".

נניח שלאדם יש שלושה חברים. כעת, אם מבין השלשה הזו, יש שניים שהם חברים - נקרא להם אליס ובוב, אז "ניצחנו", כי יש לנו שלישיה שכולם בה חברים אחד של השני. אליס ובוב חברים, ואדם חבר הן של אליס והן של בוב.

לעומת זאת, אם מבין שלושת החברים של אדם, <strong>כולם</strong> אויבים, שוב ניצחנו; כי מצאנו שלשה של אנשים שכולם אויבים. נותר לטפל במקרה שבו לאדם אין שלושה חברים אלא שלושה אויבים, אבל המקרה הזה זהה באופיו למקרה של שלושת החברים - נסו לחשוב איך צריך לשנות את הטיעון כדי שהוא יעבוד.

שאלת ההמשך, עם 10 האנשים והשלישיית חברים או רביעיית אויבים, היא מאתגרת קצת יותר. הרעיון הבסיסי הוא להשתמש איכשהו באבחנה שכבר יש לנו בדבר מה שקורה בכל שישייה.

אם כן, ניקח שוב אחד מהמשתתפים במסיבה, נקרא לו "אדם" ונתבונן בקשר שלו עם שאר האנשים. ראשית, אם יש לו לפחות שישה אויבים, "ניצחנו": כי על פי הטענה הקודמת שהוכחנו, או שיש בשישיה הזו שלישיה של חברים (ואז סיימנו) או שיש שלישיה של אויבים, ואז נוסיף לה את אדם ונקבל רביעיה של אויבים, וסיימנו.

לכן נותר להניח שלאדם יש לכל היותר חמישה אויבים, דהיינו לפחות ארבעה חברים. אם כל זוג מבין ארבעת אלו הוא אויב, סיימנו כי קיבלנו רביעיה של אויבים; אחרת יש זוג חברים - נצרף אליו את אדם וקיבלנו שלישיית חברים, וסיימנו.

זוהי כל ההוכחה. היא עשויה להיראות אד-הוקית משהו; הרבה חלוקה למקרים. עם זאת, לטעמי היא די נחמדה ואינה מסובכת עד כדי כך. בפרט, אין צורך במתמטיקה "גבוהה" כדי להגיע אליה או להבין אותה. עם זאת, החידה הזו מתקשרת באופן ישיר למתמטיקה גבוהה - היא מקרה פרטי של מה שנקרא "<a href="http://he.wikipedia.org/wiki/%D7%9E%D7%A9%D7%A4%D7%98_%D7%A8%D7%9E%D7%96%D7%99">משפט רמזי</a>". יש מספר דרכים שונות לנסח את המשפט, והמקובלת ביותר היא עבור גרפים; המשפט אומר שלכל זוג מספרים טבעיים {% equation %}n,m{% endequation %}, קיים מספר טבעי מינימלי כלשהו {% equation %}R_{n,m}{% endequation %} כך שכל גרף שמכיל יותר ממספר זה של צמתים, בהכרח יכיל אחד משניים: קבוצה של {% equation %}n{% endequation %} צמתים שכל שניים מהם מחוברים בקשת (קבוצה שכזו נקראת "קליק", Clique), או קבוצה של {% equation %}m{% endequation %} צמתים שכל שניים מהם לא מחוברים בקשת (קבוצה שכזו נקראת "קבוצה בלתי תלויה").

ה"בעיה" עם המשפט היא שהוא אינו נותן דרך קונסטרוקטיבית למצוא את הערכים של {% equation %}R_{n,m}{% endequation %} והם לא ידועים אלא עבור מספרים קטנים יחסית (מה שהוכחת המשפט עושה היא לתת מספר <strong>כלשהו</strong> שמעבר לו מובטח שתתקיים התכונה הרצויה של הגרפים; זה לא בהכרח המספר הקטן ביותר). ניתן לכתוב תוכנית מחשב שתעבור על כל הגרפים האפשריים עד גודל מסויים ותבדוק קיום של קליקות וקבוצות בלתי תלויות; אלא שיש המון גרפים שכאלו, ובכל גרף שכזה בדיקת קיום של קבוצה בלתי תלויה או קליק מגודל מסויים היא בעיה קשה יחסית, שנדרש הרבה זמן כדי לבצעה וטרם ידוע אלגוריתם יעיל שעושה זאת, ולא ברור אם יתגלה אי פעם (בניסוח ש<a href="http://www.gadial.net/?p=99">כבר דיברתי עליו </a>בבלוג - זוהי בעיה <a href="http://he.wikipedia.org/wiki/%D7%9E%D7%97%D7%9C%D7%A7%D7%AA_%D7%94%D7%A1%D7%99%D7%91%D7%95%D7%9B%D7%99%D7%95%D7%AA_NPC">NP-שלמה</a>).

החידה על המסיבה רומזת שככל הנראה {% equation %}R_{3,3}=6,R_{3,4}=10{% endequation %}; ההוכחה לא מלאה כי למרות שהראינו שהגדלים הללו מספיקים, לא הראינו שהם הכרחיים, כלומר שבגרפים קטנים יותר לא בהכרח תהיה סיטואציה כמו זו שהזכרנו. יחסית קל לעשות זאת - רק צריך להציג דוגמה נגדית אחת. נסו לעשות זאת.

נעבור כעת לפרשיית הביצה. המספר הלא ברור 14 הוא פתרון החידה - צריך לכל הפחות 14 זריקות כדי להבטיח שנדע מה הקומה המינימלית ששוברת את הביצה; אבל למרבה המזל, דווקא יש סיבה נאה למדי למספר הזה. בפרט, הוא המספר המינימלי {% equation %}k{% endequation %} שעבורו הסכום {% equation %}1+2+\dots+k{% endequation %} גדול ממאה.

ההוכחה שלי תהיה קונסטרוקטיבית במובן זה שהיא תצביע על האלגוריתם שהכרחי לנקוט בו אם רוצים להבטיח 14 זריקות. עם זאת, כדי לראות ש-14 הוא אכן המספר הנכון אטפל בבעיה באופן כללי יותר. נניח שאני רוצה לנקוט בדרך פעולה שתבטיח לי שלא אצטרך יותר מ-{% equation %}k{% endequation %} זריקות, כש-k הוא מספר טבעי כלשהו; מה אני חייב לעשות?

ובכן, הזריקה הראשונה שלי חייבת להיות מקומה שאיננה גבוהה יותר מהקומה ה-{% equation %}k{% endequation %} בדיוק. מדוע? כי נניח שזרקתי מהקומה ה-{% equation %}k+1{% endequation %} והביצה נשברה. מה עושים עכשיו? אני לא יכול להסתכן בשבירת הביצה האחרונה שנותרה לי; אם, נניח, אזרוק אותה מהקומה ה-{% equation %}k{% endequation %} והיא תישבר, לא אוכל לדעת מזה כלום - ייתכן אפילו שכבר הקומה הראשונה שוברת את הביצה. לכן אני חייב להתחיל לזרוק מהקומה הראשונה, ואז השנייה, ואז השלישית וכן הלאה. בסה"כ אצטרך {% equation %}k{% endequation %} זריקות כדי לבדוק את כל הקומות שקטנות מ-{% equation %}k+1{% endequation %}, במקרה הגרוע ביותר שבו הקומה ששוברת את הביצה היא אכן הקומה {% equation %}k+1{% endequation %} (או קומה {% equation %}k{% endequation %}, למען האמת) ולכן בסך הכל מספר הזריקות שלי  יהיה {% equation %}k+1{% endequation %} במקרה הגרוע ביותר - כלומר, לא עמדתי באתגר שהצבתי לעצמי, להשתמש ב-{% equation %}k{% endequation %} זריקות לכל היותר.

מסקנה מכל הדיון הזה: אם אני לא רוצה יותר מ-{% equation %}k{% endequation %} זריקות, אני חייב להתחיל בכך שאני זורק מהקומה ה-{% equation %}k{% endequation %} לכל היותר.

האם יש סיבה להתחיל מקומה נמוכה יותר מהקומה ה-{% equation %}k{% endequation %}? לא. כדי לראות זאת, יש להבדיל בין שני התרחישים האפשריים. אם הביצה תישבר כשנשליך אותה מקומה נמוכה יותר, אז אמנם נצליח למצוא את הקומה הנכונה בפחות מ-{% equation %}k{% endequation %} זריקות (למה?) אבל הרי כל מה שאנחנו מנסים לעשות הוא להשיג <strong>בדיוק</strong> {% equation %}k{% endequation %} זריקות במקרה הגרוע ביותר, כך שלא הרווחנו כלום במקרה זה. לעומת זאת, אם הביצה לא תישבר, אפשר לעשות את התרגיל המחשבתי הבא: לשנות את המספור של הקומות כך שקומה {% equation %}k+1{% endequation %} תיחשב לקומה מס' 1, ו"להתחיל מחדש" את המשחק שלו, עבור בניין נמוך יותר (במקום 100 קומות יהיו בו {% equation %}100-k{% endequation %} קומות), וזריקה אחת פחות. דהיינו, ננסה לפעול בצורה שמבטיחה לנו לכל היותר {% equation %}k-1{% endequation %} זריקות (כי את הזריקה הראשונה כבר ניצלנו). ברור (נכון?) שהאינטרס שלנו הוא שהבניין החדש יהיה קטן ככל הניתן, ולכן עדיף להשליך את הביצה מקומה גבוהה ככל הניתן - דהיינו, מקומה {% equation %}k{% endequation %}.

אם כן, נסכם: השיטה שלנו גורסת שמתחילים מהטלה מהקומה ה-{% equation %}k{% endequation %}. אם נשבר, אחלה; עוברים על כל הקומות הנמוכות יותר עד שהביצה נשברת (או שהיא לא, ואז התשובה היא {% equation %}k{% endequation %}). אחרת, מתחילים מחדש עם בניין יותר נמוך ורק {% equation %}k-1{% endequation %} זריקות נותרות; כלומר, הזריקה הבאה תהיה מהקומה ה-{% equation %}k-1{% endequation %} של הבניין הנמוך יותר (ובפועל - מהקומה ה-{% equation %}2k-1{% endequation %} של הבניין המקורי), וכן הלאה וכן הלאה עד שזה נגמר. זה נגמר אם הגובה של הבניין שנותר הוא פחות ממספר הזריקות שאנחנו עוד יכולים להרשות לעצמנו, ואז פשוט אפשר לעבור על כולן סדרתית.

למה זה מתורגם בפועל? בהתחלה אנחנו "מכסים" {% equation %}k{% endequation %} קומות, אחר כך {% equation %}k-1{% endequation %} קומות וכן הלאה, עד שבסוף, אם טרם סיימנו, אנחנו "מכסים" רק קומה אחת. כלומר, מספר הקומות הכולל שאנחנו מכסים הוא בדיוק {% equation %}1+2+\dots+(k-1)+k{% endequation %}. דהיינו, השיטה שלנו תעבוד עבור ה-{% equation %}k{% endequation %} שבחרנו אם ורק אם הסכום הזה הוא גדול ממספר הקומות בבניין. לכן ה-{% equation %}k{% endequation %} המינימלי שעבורו זה מתקיים הוא גם מספר הזריקות המינימלי שיידרש מאיתנו כדי לגלות את הקומה הבעייתית.

ההוכחה שאני מציע היא "אלגוריתמית" למדי; אני בטוח שקיימות הוכחות נוספות, תיאורטיות יותר, שמראות שב-13 זריקות פשוט אי אפשר לתפוס את כל האפשרויות. אשמח לשמוע כאלו.

אתגר למי שחיבב את השאלה - לחשוב איך אפשר להכליל את כל העסק למקרה שבו אין שתי ביצים אלא מספר הביצים הוא פרמטר של הבעיה, כמו מספר הקומות.

נעבור כעת לחידה הרביעית, האחרונה. כמה כבר פנו אלי עם הפתרון הנכון, אבל גם עם תמיהה מה כל כך יפה בו. ובכן, הפתרון הוא פשוט שהמתמטיקאי יחטוף חופן עלים מהעץ בלי להראות לחברו היהיר כמה הוא חטף, וישאל "כמה עלים יש כעת על העץ". אם החבר מסוגל לספור, אז ההפרש בין התוצאה שהוא יגיד עכשיו לבין התוצאה שהוא אמר קודם אמור להיות שווה למספר העלים שיש למתמטיקאי ביד.

למה לדעתי הפתרון הזה יפה? כי הוא מציג את החסכון הגדול במאמץ שחשיבה מתמטית מספקת, על ידי כך שהיא תוקפת בעיה בצורה עקיפה. מה בעצם יש לנו כאן? מצאנו <strong>זהות</strong> בין שני דברים נפרדים - מספר העלים שיש למתמטיקאי ביד, וההפרש בין שתי התחזיות של הרברבן. מכיוון שאת האובייקט הראשון קל לנו לחקור (אנחנו יודעים בדיוק כמה עלים יש לנו ביד), נובע מכך שקל לחקור גם את האובייקט השני, דהיינו קל לדעת אם יש ביסוס כלשהו לתחזיות של הרברבן או לא. כמו בחידת הנמלים שהצגתי כאן פעם, כך גם כאן - נקודת מבט טיפה שונה על הבעיה הופכת אותה ממסובכת מאוד (לך תספור את כל העלים שעל העץ) לפשוטה ביותר.