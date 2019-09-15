---
id: 134
title: "טרטורי טורים"
date: 2008-06-17 22:56:59
layout: post
categories: 
  - אנליזה מתמטית
  - בעיות מתמטיות מפורסמות
---
אכילס והצב (מי זה <a href="http://he.wikipedia.org/wiki/%D7%90%D7%9B%D7%99%D7%9C%D7%A1">אכילס</a>? גדול גיבורי יוון העתיקה; ומי זה הצב? נו, <strong>ה</strong>צב!) החליטו להתחרות בריצה (נניח, 400 מטר). אכילס רץ במהירות 10 מטרים לשנייה (36 קמ"ש), הצב "רץ" במהירות של 1 מטר לשנייה (3.6 קמ"ש - <a href="http://he.wikipedia.org/wiki/%D7%9E%D7%A1%D7%99%D7%9C%D7%AA_%D7%9B%D7%95%D7%A9%D7%A8">הליכונים</a> בדרך כלל נעלבים כשמבקשים מהם את המהירות הזו). מי מנצח? כמובן שאכילס, אלא שיש כאן טוויסט; אכילס החליט להתחשב בצב ולתת לו מקדמה של 100 מטרים. אז מי מנצח עכשיו?

למרבה הצער, אכילס עדיין מנצח - לוקחות לו 40 שניות לעבור את המרחק כולו, בעוד שהצב זקוק ל-300 שניות כדי לעבור את המרחק שנותר לו אחרי המקדמה. תרגיל קצת יותר מעניין בחשבון הוא מתי אכילס ישיג בדיוק את הצב, כלומר מתי הם יהיו באותו מיקום. לצורך כך כותבים שתי "משוואות תנועה". הנה זו של אכילס:

{% equation %}x_a(t)=10t{% endequation %}

כאן {% equation %}x_a(t){% endequation %} הוא המיקום של אכילס בזמן {% equation %}t{% endequation %} ביחס לתחילת המסלול. משוואת התנועה של הצב היא:

{% equation %}x_b(t)=100+t{% endequation %}

ואנו רוצים לגלות את ה-{% equation %}t{% endequation %} שעבורו {% equation %}x_a(t)=x_b(t){% endequation %}. כלומר:

{% equation %}10t=100+t{% endequation %}

ואחרי העברת אגפים וחילוק:

{% equation %}t=\frac{100}{9}=11\frac{1}{9}{% endequation %}

כלומר, אחרי קצת יותר מ-11 שניות אכילס משיג את הצב. לא סיפור מעניין כל כך.

האמנם?

בא פילוסוף יווני בשם <a href="http://he.wikipedia.org/wiki/%D7%96%D7%A0%D7%95%D7%9F_%D7%9E%D7%90%D7%9C%D7%90%D7%94">זנון</a> וטוען שאכילס לעולם לא יצליח לעקוף את הצב. הנה ההגיון שלו: בתחילת המירוץ, על אכילס לעבור 100 מטרים כדי להגיע אל הצב. הוא רץ אותם ומגיע לנקודה שבה היה הצב בתחילת המירוץ, אבל עד שהוא הגיע אליה, הצב כבר הספיק להתקדם קצת והגיע לנקודה חדשה. אכילס שוב יוצא לדרך בעקבות הצב ושוב מגיע למקום שבו הצב היה, אבל עד אז הצב הספיק שוב להתקדם, ושוב על אכילס להשיג אותו, וכן הלאה וכן הלאה עד אינסוף. לכן אכילס לעולם לא יעקוף את הצב.

נשמע סביר?

קל לפטור את הטיעון הזה באמירת "עזוב שטויות", אבל קשה להתעלם מכך שעל פניו אין בו שגיאה. זו דוגמה נאה לפרדוקס - טיעון שנראה לוגי לגמרי, אבל מוביל למסקנות שנראות לנו לא לוגיות. אני אישית סבור שפרדוקסים הם פשוט דוגמאות מחוכמות להוכחות בדרך השלילה - התוצאה האבסורדית שלהן אמורה להבהיר לנו שיש לנו שגיאה כלשהי בהנחות או בדרך הסקת המסקנות, ו<a href="http://he.wikipedia.org/wiki/%D7%94%D7%A4%D7%A8%D7%93%D7%95%D7%A7%D7%A1%D7%99%D7%9D_%D7%A9%D7%9C_%D7%96%D7%A0%D7%95%D7%9F">הפרדוקס הזה,</a> שזכה לשם הסביר "פרדוקס אכילס והצב", אינו שונה.

שני פרדוקסים נוספים מפורסמים שהציע זנון הם בעלי אופי דומה. הראשון טוען שגם אם אכילס מתחרה נגד עצמו הוא לעולם לא יסיים את המירוץ, או אפילו יתחיל אותו: לפני שהוא יגיע לנקודת הסיום, עליו לעבור בנקודת האמצע - נקודת 200 המטרים. לפני שהוא מגיע אליה, עליו להגיע לנקודת 100 המטרים; לפניה, לנקודת 50 המטרים; וכן הלאה וכן הלאה. כלומר, לכל נקודה שרק נרצה על המסלול אפשר למצוא נקודה אחרת שאליה הוא צריך להגיע קודם. הפרדוקס הזה נקרא "פרדוקס הדיכוטומיה" - דיכוטומיה פירושה "חלוקה לשניים" וגם כאן מוצאים את הנקודה הקודמת שדרכה אכילס צריך לעבור על ידי חלוקה לשניים.

הפרדוקס השלישי - "פרדוקס החץ" - תמוה עוד יותר. נניח שיש לנו חץ שמתעופף לאי שם. נקפיא לרגע את העולם, כלומר נסתכל עליו בנקודת זמן מסויימת. החץ מן הסתם לא נע ב"הקפאה" הזו. אבל זה נכון לכל נקודת זמן - ומכאן שהחץ לא נע אף פעם.

לפרדוקסים לא נמצא מעולם "פתרון" שמקובל על הכלל, והם העסיקו הן את היוונים והן את הפילוסופים של ימי הביניים. עם זאת, לקראת סוף המאה ה-17 ותחילת המאה ה-18 הומצא ענף מתמטי שתקף באופן חזיתי את כל ענייני ה"חלוקה עד לאינסוף" הללו - <a href="http://he.wikipedia.org/wiki/%D7%97%D7%A9%D7%91%D7%95%D7%9F_%D7%90%D7%99%D7%A0%D7%A4%D7%99%D7%A0%D7%99%D7%98%D7%A1%D7%99%D7%9E%D7%9C%D7%99">החשבון האינפיניטסימלי</a>. אם מנסחים את הפרדוקסים של זנון בלשון החשבון האינפיניטסימלי (בפרט, בניסוח המודרני והמדוייק שלו, שאליו אחראים המתמטיקאים בני המאה ה-19 ובפרט <a href="http://he.wikipedia.org/wiki/%D7%A7%D7%90%D7%A8%D7%9C_%D7%95%D7%99%D7%99%D7%A8%D7%A9%D7%98%D7%A8%D7%90%D7%A1">ויירשטראס</a> ו<a href="http://he.wikipedia.org/wiki/%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%D7%99%D7%9F_%D7%9C%D7%95%D7%90%D7%99_%D7%A7%D7%95%D7%A9%D7%99">קושי</a>) הפרדוקסליות שבהם נעלמת, והם הופכים להיות לא יותר מאשר שיעור בהסקת מסקנות חפוזה. לאנשים כמוני, שמתעניינים במתמטיקה יותר מאשר בפילוסופיה, זה מספיק; קיימים אנשים שסבורים שהחשבון האינפיניטסימלי לא פתר כלום. הדוגמה הבולטת בה נתקלתי היא פרופ' זאב בכלר, שתוקף חזיתית את החשבון האינפינטסימלי ואת מושג ה"סכום של טור אינסופי" שתכף אציג, בספרו "<a href="http://he.wikipedia.org/wiki/%D7%A9%D7%9C%D7%95%D7%A9_%D7%9E%D7%94%D7%A4%D7%9B%D7%95%D7%AA_%D7%A7%D7%95%D7%A4%D7%A8%D7%A0%D7%99%D7%A7%D7%A0%D7%99%D7%95%D7%AA">שלוש מהפכות קופרניקניות</a>". אנסה להקדיש פוסט נפרד למתקפה הזו, ואסתפק בינתיים בלהגיד שהטיעון המרכזי שלו, עד כמה שאני מבין אותו, הוא שהחשבון האינפיניטסימלי, תחת שיפתור את הפרדוקסים, ממציא "שפה חדשה" שבה אי אפשר בכלל לתאר אותם.

לעת עתה, מכיוון שאני מציג את הפרדוקסים כמוטיבציה להגדרת <a href="http://he.wikipedia.org/wiki/%D7%98%D7%95%D7%A8_%D7%90%D7%99%D7%A0%D7%A1%D7%95%D7%A4%D7%99#.D7.98.D7.95.D7.A8.D7.99.D7.9D_.D7.90.D7.99.D7.A0.D7.A1.D7.95.D7.A4.D7.99.D7.99.D7.9D">טורים אינסופיים</a>, אתעסק רק בוריאציה על פרדוקס הדיכוטומיה, שמובילה אותי הישר אל מושג הטור האינסופי. הוריאציה פשוטה - במקום לומר "לפני שאכילס עובר חצי מהדרך הוא צריך לעבור רבע" אני אומר "אחרי שאכילס עבר חצי מהדרך, נותר לו לעבור חצי; אחרי שעבר עוד רבע, עדיין נותר לו רבע נוסף; אחרי שעבר עוד שמינית, נותרה לו עדיין שמינית נוספת" וכן הלאה. המסקנה ברורה - תמיד יישאר לו עוד "קצת" מרחק לעבור ולכן הוא אף פעם לא יגיע לקצה. זו בעצם וריאציה על פרדוקס אכילס והצב, אבל פשוטה קצת יותר.

בדיחה (גסה ושוביניסטית) ידועה מספרת על מתמטיקאי ופיזיקאי (או מהנדס) שנמצאים בסיטואציה שכזו - הם נמצאים בתחילת חדר ובקצה השני ישנה בחורה שאליה הם רוצים להגיע. המתמטיקאי מוותר מראש על הבחורה כי על פי הבעיה שהצגתי כרגע, לא משנה כמה הוא ילך לכיוון הבחורה הוא לעולם לא יגיע. לעומת זאת הפיזיקאי מתחיל לצעוד. כשהמתמטיקאי שואל אותו למה הוא בכלל מנסה, הפיזיקאי עונה לו "נכון שלעולם לא אגיע, אבל אני אתקרב מספיק לכל צורך מעשי".

הבדיחה הזו לא הוגנת במיוחד, מכיוון שדווקא המתמטיקאים הם שמקדשים את גישת ה"קרוב מספיק", והביאו את הפורמליזם שלה לכדי אמנות. רעיון ה"קרוב מספיק" הזה הוא למעשה הבסיס לחשבון האינפיניטסימלי כולו.

הבה ונתבונן בבעיה מבחינה מתמטית. כדי להגיע לקצה השני צריך לעבור מרחק של 1/2, ואחריו מרחק של 1/4, ואחריו מרחק של 1/8 וכן הלאה. כלומר, אפשר לתאר את המרחק הכולל שיש לעבור באמצעות טור אינסופי:

{% equation %}\sum_{n=1}^\infty\frac{1}{2^n}=\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\dots{% endequation %}

מה סכום הטור הזה? אינטואיטיבית, מפתה לצעוק "אינסוף" פשוט כי יש לנו אינסוף מחוברים חיוביים. האם זה גם נראה לנו הגיוני? הרי אם אנו חושבים על סכום הטור האינסופי הזה בתור המרחק הכולל שנעבור, פירוש הדבר הוא שכדי לעבור מרחק של 1 עלינו לעבור מרחק אינסופי - וזה דווקא מנוגד לאינטואיציה. לכן נשאלת השאלה - אם לדבר הזה יש סכום שהוא מספר ממשי סופי, מה הוא?

כמובן שאני מתחמק כאן מהשאלה האמיתית, הפילוסופית - מה זה בכלל "סכום"? מה פשר המילה הזו? כשמדובר במספר סופי של איברים, כבר הגדרתי את המשמעות המקובלת של המילה: מה שמתקבל כשמחברים את כל איברי הטור. כאן מובלעת הנחה סמוייה - שאכן אפשר לחבר אותם, למרות ש"חיבור" היא פעולה בינארית, כלומר כזו שמוגדרת רק על שני איברים. הסיבה לכך שאפשר לחבר שלושה איברים, היא שאפשר לבצע את החיבור ב"שני שלבים", שבכל אחד מהם מחברים רק שני איברים: כדי לחשב את הסכום x+y+z קודם אני מחשב את x+y, מקבל מספר שאסמן w, ואז מחשב את w+z, ולמספר שאני מקבל אני קורא "הסכום של x,y,z". שימו לב שהייתי מקבל את אותה תוצאה גם אם הייתי מחבר את y ל-z ואת התוצאה מחבר ל-x; זו התופעה שמכונה "חוק הקיבוץ", או "אסוציאטיביות החיבור", והיא אינה תמיד תקפה - למשל, בחישוב x-y-z יש חשיבות גדולה לשאלה איזו פעולה מתבצעת קודם (ומכיוון שמבצעים קודם את x-y, הפעולה ה"שמאלית" יותר, אומרים שחיסור הוא בעל "אסוציאטיביות שמאלית").

איך סוכמים ארבעה איברים? ובכן, סוכמים את שני האיברים הראשונים, מחליפים אותם בתוצאה הסכום, ונותרים עם סכום של שלושה איברים, שאנחנו כבר יודעים לחשב. ואיך מחשבים סכום של חמישה? אותו כנ"ל - מחברים שניים, נותרים עם סכום של ארבעה, ובו כבר יודעים לטפל, וכו' וכו'. על דרך הפעולה הזו אומרים שאפשר <strong>באינדוקציה</strong> להגדיר את החיבור עבור כל מספר סופי של מחוברים. מי מכם שזוכרים אינדוקציות מתמטיות בוודאי יצליחו לראות את הקשר - הגדרנו חיבור עבור n=2 ("בסיס") והראינו איך בהינתן חיבור עבור n איברים, אנחנו מסוגלים להגדיר אותו עבור n+1, ומכאן שניתן להגדיר אותו עבור כל n מחוברים.

כל זה טוב ויפה, אבל בכלל לא עובד כשמדובר באינסוף איברים. נניח שאנחנו מנסים להשתמש באותו רעיון עבור אינסוף איברים - אנחנו מחברים את שני האיברים הראשונים, מקבלים תוצאת ביניים, ו...? מה עכשיו? האם עברנו למקרה פשוט יותר? לא. גם כשמחליפים את שני האיברים הראשונים בתוצאת החיבור שלהם עדיין נותרנו עם אותה בעיה בדיוק - חיבור של אינסוף איברים.

כאן מתפצלות דרכי הפעולה שלנו לשלוש. הדרך האחת היא להרים ידיים, להגיד "אין לי מושג איך מגדירים סכום עבור אינסוף איברים", וללכת לישון. זו דרך פעולה לגיטימית לגמרי; אם אין לנו רעיון טוב איך לייחס משמעות למילה מסויימת בהקשר מסויים, אין הכרח לעשות זאת.

הדרך השנייה היא להתעקש שיש משמעות למילה "סכום" עבור אינסוף איברים אבל לא להסביר מהי. אולי לקבוע שרירותית שהסכום הוא "תמיד אינסוף", או שמדובר בדבר אלוהי ואין לחקור בו. ייתכן שארחיב על הדרך הזו בפוסט הבא, אבל לעת עתה אסתפק בכך שאגיד שלדעתי היא פסולה מעיקרה. כשעוסקים במתמטיקה, לדבר על משהו מבלי להגדיר אותו בצורה ברורה ושאינה משתמעת לשני פנים פירושו שהפסקת לעסוק במתמטיקה ועברת, למצער, לפילוסופיה, אם לא לטרחנות כפייתית.

נותרנו עם הדרך השלישית, שבה מנסים להציע הגדרה שבמובן מסויים "תכליל" את ההגדרה המקורית עבור סכום סופי, ותנסה להתבסס עליה ככל האפשר. הגישה הזו, שאציג כעת, מתעניינת בדיוק באותם "סכומי ביניים" שכבר הצגתי; מה שמתקבל אחרי שסוכמים את שני האיברים הראשונים, שלושת הראשונים, ארבעת הראשונים וכן הלאה. לכל סכום ביניים כזה קוראים <strong>סכום חלקי</strong> של הטור האינסופי.

כדי לדבר על הסכומים החלקיים כדאי למצוא דרך נוחה להציג את הסכום החלקי ה"כללי", ה-n-י במספר, זה שמתקבל אחרי שסכמנו את n האיברים הראשונים:

{% equation %}\frac{1}{2}+\frac{1}{4}+\dots+\frac{1}{2^n}=?{% endequation %}

למרבה המזל, <strong>במקרה של הטור הספציפי הזה</strong> זה קל למדי, שכן הטור הזה הוא <a href="http://he.wikipedia.org/wiki/%D7%A1%D7%93%D7%A8%D7%94_%D7%94%D7%A0%D7%93%D7%A1%D7%99%D7%AA">טור הנדסי</a>, מהסוג שמכריחים תלמידים אומללים להיאבק בו בבית הספר. כל איבר בטור מתקבל על ידי הכפלה של האיבר הקודם ב-1/2, ויש שיטה פשוטה למדי למציאת הסכום שלו. לא אציג אותה כרגע (תרגיל!), אלא אסתפק בכתיבת הסכום של הטור הספציפי הזה: {% equation %}1-\frac{1}{2^n}{% endequation %} (למעשה, רגע של מחשבה יבהיר שזה אכן הסכום ואין ממש צורך בנוסחאות לטורים הנדסיים - גם זה תרגיל).

עברנו אם כן מדיבור על טור, לדיבורים על סדרה, שאנו יודעים כיצד נראה האיבר הכללי שלה. כעת מה שמעניין אותנו הוא לאן הסדרה הזו "הולכת". האם זה נראה כאילו יש לה יעד מובהק, שאליו היא כל הזמן מתקרבת? או שההתנהגות שלה היא "מופרעת" ולא עושה רושם שקיים יעד כזה? והאם בכלל אפשר להגדיר פורמלית טענה שכזו?

המתמטיקאים שפירמלו את החשבון האינפיניטסימלי במאה ה-19 חשבו שאפשר להגדיר זאת פורמלית. המושג שהמציאו נקרא "<a href="http://he.wikipedia.org/wiki/%D7%92%D7%91%D7%95%D7%9C_(%D7%9E%D7%AA%D7%9E%D7%98%D7%99%D7%A7%D7%94)">גבול</a>", והוא כנראה אחד מהמושגים (ויותר מכך - ה<strong>רעיונות</strong>) החשובים במתמטיקה המודרנית. עם זאת, הוא עדיין "פשוט" מספיק כדי שניתן יהיה להציג אותו לסטודנטים בסמסטר הראשון שלהם - אך הוא מורכב מספיק כדי שהם ייאלצו להיאבק איתו. לא אציג אותו כאן בצורה מדוייקת כעת; אדחה זאת לפוסט אחר, טכני יותר, שיציג את ההגדרה הפורמלית. לעת עתה אסתפק בהגדרה מילולית: גבול של סדרת מספרים ממשיים הוא מספר ממשי שמקיים את התכונה הבאה: אם ניקח סביבה שלו (כל המספרים שמרחקם ממנו לא עולה על גודל קבוע מסויים), ולא משנה כמה קטנה תהיה, מובטח לנו שכל אברי הסדרה יהיו שם, פרט אולי למספר סופי שלהם. דהיינו - החל ממקום מסויים בסדרה, <strong>כל</strong> איבריה יהיו קרובים לגבול, לכל מידת קרבה שנרצה (פרט למידת הקרבה שמכריחה את כל אברי הסדרה החל מאותו מקום להיות <strong>שווים</strong> לגבול).

מרחק בין שני מספרים ממשיים הוא פשוט הערך המוחלט של ההפרש שלהם. לכן, חישוב קצר יראה שהמרחק בין המספר 1 ובין האיבר ה-n-י של הסדרה הוא בדיוק {% equation %}\frac{1}{2^n}{% endequation %}. ככל ש-n גדול יותר, כך המרחק הזה קטן יותר, והוא מתקרב לאפס עוד ועוד (אך אף פעם אינו נעלם לחלוטין). מכאן אפשר להסיק שגבול הסדרה הזו הוא 1. כאן נגמרת המתמטיקה והפילוסופיה מתחילה מחדש: מה זה אומר, שהגבול הוא 1? האם זה אומר שהסדרה "מגיעה" לשם? האם המספר הזה הוא האיבר ה"אחרון" של הסדרה? שוב - לא אכנס כעת לשאלות אלו. לעת עתה, די בכך שאנו <strong>מגדירים</strong> את סכום הטור האינסופי להיות הגבול של סדרת הסכומים החלקיים, ולכן עבור הטור שלעיל, התוצאה היא 1.

כעת אפשר סוף סוף לחזור אל <a href="http://www.gadial.net/?p=133">...0.999 מיודענו</a>, ולפיתוחים עשרוניים באופן כללי. באופן כללי, כל מספר ממשי מתואר בתור טור מהצורה הבאה:

{% equation %}\sum_{i=0}^k a_i10^i +\sum_{n=1}^\infty a_{-n}10^{-n}{% endequation %}

הסכום הראשון, הסופי, מתאר את כל מה שקורה משמאל לנקודה העשרונית. {% equation %}a_i{% endequation %} מייצג את הספרה ה-i משמאל לנקודה (כשמתחילים את הספירה מ-0) וכזכור, הספרה במקום ה-0 מייצגת אחדות, במקום ה-1 מייצגת עשרות, במקום 2 מייצגת מאות, וכדומה - הספרה במקום ה-i מייצגת את מספר הפעמים בהן עשר בחזקת i מופיע במספר.

הסכום השני, האינסופי, מתאר את מה שקורה מימין לנקודה העשרונית, מקום בו יכולות להופיע אינסוף ספרות (לא חייבות להופיע אינסוף ספרות - במקרה זה, החל ממקום מסויים כל ה-{% equation %}a_{-n}{% endequation %} יהיו אפסים). אני נותן ל-a-ים אינדקס "שלילי" כדי להדגיש את העובדה שהם מימין לנקודה העשרונית ולא משמאל לה. כזכור, מימין לנקודה העשרונית מה שהספרות מייצגות הוא חזקות שליליות של עשר - עשירית, מאית, אלפית וכדומה.

כעת, המספר שמיוצג על ידי הפיתוח העשרוני הזה <strong>מוגדר</strong> להיות סכום שני הטורים הללו, כאשר סכום הטור האינסופי <strong>מוגדר</strong> בדיוק בצורה שתיארתי - סכומים חלקיים, גבול, כל העסק הזה. אפשר כמובן לשאול מדוע מובטח לנו שיש גבול לטור הזה - התשובה היא שמדובר בשאלה כלל לא טריוויאלית, אליה כבר התייחסתי בעבר (כשהוצגה בניסוח קצת שונה) ואתייחס אליה באחד מהפוסטים הבאים. לעת עתה מספיק לומר שכאשר עוסקים במספרים ממשיים, אז על פי הצורה שבה המספרים הממשיים נבנו ("הוגדרו"), מובטח לנו שהטור הזה תמיד מתכנס (אינטואיציה כלשהי מדוע הטור מתכנס - החזקות השליליות של עשר שבהן מוכפל כל איבר בטור "מקטינות" את השינויים שהטור עובר מהר מאוד).

אם כן, מהו ...0.999? הפיתוח של המספר הזה לא כולל ספרות משמאל לנקודה העשרונית, והצורה של הספרות מימין מאוד פשוטה, כך שניתן לחשב את הטור שלו באופן כמעט ישיר. הטור הוא {% equation %}\sum_{n=1}^\infty\frac{9}{10^n}=9\cdot \sum_{n=1}^\infty\frac{1}{10^n}{% endequation %}. למזלנו, הטור שקיבלנו הוא טור הנדסי, שמנתו {% equation %}\frac{1}{10}{% endequation %} והאיבר הראשון שלו {% equation %}\frac{1}{10}{% endequation %}. כשאעסוק בהגדרה הפורמלית של הגבול אוכיח גם, פורמלית, כי לטור הנדסי אינסופי עם איבר ראשון {% equation %}a_1{% endequation %} ומנה {% equation %}q{% endequation %}, סכום הטור הוא בדיוק {% equation %}\frac{a_1}{1-q}{% endequation %}, בתנאי ש-{% equation %}q{% endequation %} בערכו המוחלט אינו גדול או שווה ל-1. מכאן נקבל שסכום הטור במקרה שלנו הוא:

{% equation %}9\cdot\sum_{n=1}^{\infty}\frac{1}{10^{n}}=9\cdot\frac{1}{10}\cdot\frac{1}{1-\frac{1}{10}}=\frac{9}{10}\cdot\frac{1}{\frac{9}{10}}=\frac{9}{10}\cdot\frac{10}{9}=1{% endequation %}

זה הכל. עניין של הגדרה, וידע בסיסי של התכנסות טורים הנדסיים, וסוגיית ...0.999 נפתרת בצורה פורמלית לגמרי, וללא עוררין. היחידים שיחלקו על ההוכחה הזו הם כאלו שאינם מסכימים עם ה<strong>הגדרה</strong> של מושג הפיתוח העשרוני בכלל, ושל אוסף הסימבולים ...0.999 בפרט. לטעמי, זו גם אי ההסכמה היחידה שבכלל אפשרית במתמטיקה, ואולי מכאן נובע סוד כוחה; בפוסט הבא אנסה להרחיב עוד קצת על אלו שדוחים את הגדרותיה של המתמטיקה.