---
id: 1034
title: "מה זו סיבוכיות תקשורת?"
date: 2011-03-01 20:35:00
layout: post
categories: 
  - תורת הסיבוכיות
tags: 
  - סיבוכיות תקשורת
  - פשטות היא תחכום
---
בתורת הסיבוכיות מדברים על השאלה "איזו כמות של משאבים נדרשת בשביל לבצע חישוב מסויים?". לרוב המשאבים הם זמן או זכרון מחשב; אני רוצה לדבר הפעם על מדד סיבוכיות שונה למדי באופיו, שהוא הבסיס לתחום יפה ומעניין בתורת הסיבוכיות - סיבוכיות תקשורת.

הרעיון הבסיסי הוא זה: יש לנו שני "שחקנים", אליס ובוב. אליס מחזיקה בקלט כלשהו {% equation %}x{% endequation %} ובוב מחזיק בקלט כלשהו {% equation %}y{% endequation %}. אליס ובוב רוצים לחשב פונקציה כלשהי בשני משתנים, {% equation %}f\left(x,y\right){% endequation %}. לצורך כך, ברור שחייב לעבור מידע כלשהו מאליס אל בוב ולהפך - אלא אם {% equation %}f{% endequation %} טריוויאלית למדי, לא ייתכן שאליס תוכל לחשב את {% equation %}f{% endequation %} בלי לדעת <strong>משהו</strong> על {% equation %}y{% endequation %}, ואותו הדבר עבור בוב ו-{% equation %}x{% endequation %}. לכן, בהינתן {% equation %}f{% endequation %}, עולה השאלה - כמה מידע אליס ובוב צריכים להחליף ביניהם כדי שיוכלו לחשב את {% equation %}f{% endequation %}?

כדי לפשט לעצמנו את החיים נניח כי הן {% equation %}x{% endequation %} והן {% equation %}y{% endequation %} הן מחרוזות של {% equation %}n{% endequation %} ביטים (ביט הוא או 0 או 1). השאלה שנשאלת היא כמה ביטים של תקשורת חייבים הצדדים להחליף ביניהם לפני ששניהם ידעו את {% equation %}f\left(x,y\right){% endequation %}. ברור שאם אליס תשלח לבוב את {% equation %}x{% endequation %} בשלמותו ובוב ישלח לאליס בשלמותו את {% equation %}y{% endequation %}, כל אחד מהם יוכל לחשב את {% equation %}f{% endequation %} לבד וחסל. האינטואיציה שמתעוררת די מהר היא שהם יהיו חייבים לעשות משהו בסגנון, אלא אם הפונקציה ממש מטופשת. לכן אני רוצה להתחיל את הדיון בדוגמה שמראה שזה ממש לא נכון - פונקציה מעניינת בהחלט, שסיבוכיות התקשורת שלה נמוכה באופן מפתיע.

הדוגמה היא חישוב חציון. חציון של קבוצת מספרים ("קבוצה", לא במובן התורת-קבוצותניקי הרגיל - אותו איבר יכול להופיע בקבוצה כמה פעמים. פורמלית המתמטיקאים קוראים לזה Multiset) הוא מספר שקטן בדיוק ממחציתם של המספרים, וגדול בדיוק ממחציתם של המספרים. לא תמיד זה אפשרי - למשל, בקבוצה {% equation %}\left\{ 1,2,3,4\right\} {% endequation %} אין חציון אלא שני "כמעט חציונים", {% equation %}2{% endequation %} ו-{% equation %}3{% endequation %}. במקרה הזה נאמר שרירותית ש-{% equation %}2{% endequation %} הוא החציון. בקבוצה {% equation %}\left\{ 3,6,2,2,4\right\} {% endequation %} קל לראות ש-3 הוא החציון, וכדומה.

כעת הן לאליס והן לבוב יהיו קבוצות של מספרים מ-1 עד {% equation %}n{% endequation %}. קבוצה כזו אפשר לייצג בעזרת {% equation %}n{% endequation %} ביטים: הביט ה-{% equation %}i{% endequation %} הוא 1 אם המספר {% equation %}i{% endequation %} שייך לקבוצה ו-0 אחרת. למשל, הקבוצה {% equation %}\left\{ 2,4,5\right\} {% endequation %} מיוצגת על ידי המחרוזת {% equation %}01011{% endequation %}. {% equation %}f\left(x,y\right){% endequation %} יהיה פשוט מספרו של החציון של הקבוצות {% equation %}x\cup y{% endequation %} (שוב, אם יש איבר זהה ב-{% equation %}x{% endequation %} וב-{% equation %}y{% endequation %}, באיחוד הוא יופיע פעמיים). כדי לייצג את המספר הזה צריך {% equation %}\lg n{% endequation %} ביטים - למעשה, כדי שאליס תשלח לבוב מספר כלשהו צריך {% equation %}\lg n{% endequation %} ביטים. מה שמפתיע כאן הוא שכדי לחשב את החציון המשותף לא צריך הרבה יותר מאשר {% equation %}\lg n{% endequation %} ביטים - סיבוכיות התקשורת של {% equation %}f{% endequation %} היא {% equation %}O\left(\lg n\right){% endequation %}.

כמו שקורה לעתים קרובות בסיבוכיות, התוצאה הזו היא מסוג הדברים שכשאני שומע עליהם לראשונה אני חושב "אין סיכוי. לא נכון. שקר וכזב. בלתי אפשרי. אין שום דרך לעשות את זה". היופי בסיבוכיות הוא איך שמוצאים דרך לעשות את זה. הפתרון כאן הוא אמנם מחוכם ויפה למדי אבל לא מסובך במיוחד, ואני מקווה לא לאבד קוראים במהלכו. אגב, אני ממליץ לכולכם לנסות ולחשוב על הבעיה לפני שתקראו את הפתרון; כפי שקורה לעתים קרובות בעניינים הללו, עד שלא יושבים וחושבים אישית על הבעיה קשה להבין עד כמה היא קשה/טריקית ומדוע הפתרון שלה הוא יפה.

ראשית, מה שאליס ובוב יעשו כדי לפשט לעצמם את החיים הוא לוודא שהן {% equation %}x{% endequation %} והן {% equation %}y{% endequation %} שניהם מאותו הגודל ושגודל זה הוא חזקה של 2. לצורך כך כל אחד ישלח לשני את גודל הקבוצה שלו; מכיוון שהגודל המקסימלי הוא {% equation %}n{% endequation %}, צריך {% equation %}\lg n{% endequation %} ביטים לשם כך. כדי להגדיל את הקבוצות לגודל הרצוי אפשר פשוט להוסיף זוגות של {% equation %}1,n{% endequation %} ככל שיידרש - להוסיף 1 ו-{% equation %}n{% endequation %} לקבוצה לא יכול לשנות את החציון שלה. אם גודל הקבוצה היה אי זוגי צריך יהיה גם להוסיף {% equation %}n{% endequation %} פעם אחת לבדו. שימו לב שלא מגדילים יותר מדי את {% equation %}x,y{% endequation %} - לכל היותר פי 2. זה לא משפיע על הסיבוכיות האסימפטוטית, ולכן מעתה ואילך ארשה לעצמי להניח ש-{% equation %}n{% endequation %} הוא חזקה של 2.

עכשיו נציג פרוטוקול "גרוע", שעובד בסיבוכיות תקשורת {% equation %}O\left(\lg^{2}n\right){% endequation %}. אחר כך נשפר אותו. "גרוע" במרכאות כי גם הסיבוכיות הזו היא נמוכה מאוד ביחס לחסם העליון הנאיבי ({% equation %}O\left(n\right){% endequation %}). הרעיון הוא שאליס ובוב יתחזקו, בנפרד, קבוצות של "מועמדים להיות החציון" שלהם - נסמן אותן ב-{% equation %}x^{\prime}{% endequation %} וב-{% equation %}y^{\prime}{% endequation %}, ובהתחלה הן יכילו את כל {% equation %}x,y{% endequation %}. בכל סיבוב של הפרוטוקול אליס ובוב יצליחו, באמצעות שליחת הודעות כלשהי, לקצוץ בחצי את גודל קבוצות המועמדים. מה שהם ישלחו, בפשטות, יהיו החציונים הנוכחיים של {% equation %}x^{\prime}{% endequation %} ו-{% equation %}y^{\prime}{% endequation %}. צריך {% equation %}\lg n{% endequation %} ביטים בשביל לשלוח כל אחד מהם. בואו נניח שאליס שלחה את {% equation %}a{% endequation %} ובוב שלח את {% equation %}b{% endequation %} והם רואים ש-{% equation %}a&lt;b{% endequation %}. מה עכשיו? ובכן, ברור שהחציון שאותו מחפשים נמצא אי שם בין {% equation %}a{% endequation %} ל-{% equation %}b{% endequation %}, שכן אם מספר כלשהו קטן מ-{% equation %}a{% endequation %} אז הוא לא גדול יותר מאשר מחצית מאברי {% equation %}x^{\prime}{% endequation %}, ובוודאי שאינו גדול יותר מאשר ממחצית מאברי {% equation %}y^{\prime}{% endequation %} ולכן יגם ממחצית אברי האיחוד שלהם. באותו אופן מספר שגדול מ-{% equation %}b{% endequation %} אינו יכול להיות החציון.

כעת, אליס תעיף מ-{% equation %}x^{\prime}{% endequation %} מחצית מהאיברים - את הקטנים ביותר. בוב יעיף מ-{% equation %}y^{\prime}{% endequation %} מחצית מהאיברים - הגדולים ביותר. מכיוון שאליס העיפה איברים שקטנים מהחציון האמיתי, ובוב העיף איברים שגדולים מהחציון האמיתי, והם העיפו את אותו מספר האיברים, אז החציון המקורי יהיה גם החציון של איחוד הקבוצות המקוצצות, שכעת גודלן הוא חצי ממה שהיה קודם.

אותו תעלול עושים אבל הפוך אם {% equation %}b&lt;a{% endequation %}. אם {% equation %}a=b{% endequation %} אז זהו בוודאי החציון, שכן לפני רגע אמרנו שהוא נמצא בין {% equation %}a{% endequation %}ל-{% equation %}b{% endequation %}.

יש {% equation %}O\left(\lg n\right){% endequation %} סיבובים לפרוטוקול הזה ובכל אחד מהם כל אחד מהצדדים שולח מספר וזה דורש {% equation %}O\left(\lg n\right){% endequation %} ביטים. סך הכל נשלחים {% equation %}O\left(\lg^{2}n\right){% endequation %} ביטים, אבל זה לא מספיק לנו; אנחנו רוצים לשפר.

למרבה המזל, השיפור מאוד קל, ודורש רק אבחנה אחת, מקסימה, על אופן פעולתו של הפרוטוקול הזה. נשים לב שאליס ובוב לא באמת רוצים לדעת את {% equation %}a,b{% endequation %} האחד של השני - רק לדעת מי מהם גדול יותר. כדי לדעת את זה, מספיק לשלוח את {% equation %}a,b{% endequation %} <strong>ביט אחרי ביט</strong>, החל מהביט המשמעותי ביותר. כלומר - כל מספר מיוצג על ידי סדרה של בדיוק {% equation %}\lg n{% endequation %} ביטים, וייתכן שחלק מהביטים המובילים הם 0 - הן אליס והן בוב מתחילים לשלוח ביטים החל מהשמאלי ביותר. כל עוד יש שוויון, הם ממשיכים לשלוח את הביט הבא; ברגע שאין שוויון הם יודעים בדיוק מי הגדול יותר (זה שהביט שלו היה 1).

כפי שכבר אמרנו, אחרי הקיצוץ שאליס ובוב מבצעים, האיברים היחידים ששורדים בקבוצות שלהם הם איברים שהם בין {% equation %}a{% endequation %} ו-{% equation %}b{% endequation %}. בשלב של הקיצוץ אליס ובוב כבר מכירים חלק מהביטים של {% equation %}a{% endequation %} ו-{% equation %}b{% endequation %}: כל הביטים המשמעותיים ביותר שעליהם {% equation %}a,b{% endequation %} מסכימים. הפאנץ' הסופי הוא שגם <strong>כל מי שבין </strong>{% equation %}a{% endequation %} ו-{% equation %}b{% endequation %} מסכים על אותם ביטים. אם {% equation %}a=0100{% endequation %} (הידוע בשמו הארצי "4") ו-{% equation %}b=0111{% endequation %} (הידוע בשמו הארצי "7"), אז המספרים היחידים שביניהם הם {% equation %}0101,0110{% endequation %} (5 ו-6) ושניהם מסכימים עם {% equation %}a,b{% endequation %} על התחילית {% equation %}01{% endequation %}. מכאן שאין שום צורך לשלוח את הביטים הללו מחדש בסיבוב הבא של הפרוטוקול - אליס ובוב ימשיכו לשלוח ביטים החל מהספרה המעניינת הבאה.

מכיוון שכל מספר מיוצג על ידי {% equation %}\lg n{% endequation %} ביטים, ואליס ובוב משווים <strong>פעם אחת בכל הפרוטוקול</strong> ביט עבור כל אחד מהמיקומים האפשריים, הם סך הכל מחליפים {% equation %}O\left(\lg n\right){% endequation %} ביטים, כנדרש.

הדוגמה הזו מראה עד כמה אפשר להיות מתוחכמים לפעמים בפתרון בעיות שנראות בלתי אפשריות לפתרון שאינו אלמנטרי. זו אולי ההמחשה הטובה ביותר לחיים הקשים שיש לחוקרי תורת הסיבוכיות; המטרה שלהם היא להראות חסמים <strong>תחתונים</strong>, כלומר שבעיה כלשהי אינה ניתנת לפתרון בסיבוכיות נמוכה, <strong>ולא משנה מה עושים</strong>. לשם כך הם צריכים איכשהו לטפל בכל הטריקים האפשריים "בו זמנית", אבל בגלל שאפשר להשתמש בטריקים מאוד, מאוד מחוכמים, אין ממש סיכוי לתת טיעון שמקיף את כולם בצורה ישירה. לכן עיקר המאמץ מתמקד בשיטות כלליות וגנריות יותר שמראות חסמים תחתונים באופן שחומק מעיסוק בפרטים הספציפיים של פתרונות ספציפיים.

הרעיון הבסיסי בניתוח כללי של פרוטוקולים מהסוג שתיארתי למעלה הוא לחשוב עליהם כעץ, שבו בכל צומת או תורה של אליס לדבר, או תורו של בוב. כל אחד מהם אומר 0 או 1 כפונקציה של הקלט שלו עצמו ושל הצומת הנוכחי בעץ (כלומר, לצמתים שונים בעץ מתאימות פונקציות אחרות שאומרות להם איך לדבר). לצומת יש שני בנים - אחד שאליו עוברים אם נאמר 0, והשני שאליו עוברים אם נאמר 1. העלים של העץ מכילים את התוצאות של הפרוטוקול - לצורך פשטות נניח שמדובר רק על ביט בודד של תשובה.

האבחנה המרכזית כאן היא שאם על שני זוגות קלטים שונים {% equation %}\left(x_{1},y_{1}\right){% endequation %} ו-{% equation %}\left(x_{2},y_{2}\right){% endequation %} אליס ובוב מגיעים לאותו צומת בפרוטוקול, אז הם מגיעים לאותו הצומת גם עבור הזוג {% equation %}\left(x_{1},y_{2}\right){% endequation %}. נסו להוכיח את הטענה הזו - דרך פשוטה אחת היא להוכיח באינדוקציה על עומק הצומת. האינטואיציה פה היא שאם על שני הזוגות המקוריים אליס ובוב הגיעו לאותו צומת בפרוטוקול, זה אומר שהתקשורת שנשלחה ביניהם הייתה זהה בשני המקרים, ולכן אליס לא יכולה להבדיל, באמצעות התקשורת שבוב שלח לה עד שהם הגיעו לצומת המדובר, בין זה שיש לו {% equation %}y_{1}{% endequation %} וזה שיש לו {% equation %}y_{2}{% endequation %}, כל עוד התשובות שהיא עצמה נותנת מתאימות לקלט {% equation %}x_{1}{% endequation %} או {% equation %}x_{2}{% endequation %} שיש לה.

המסקנה מהטענה הזו היא שיש לאוסף התוצאות האפשריות של הפרוטוקול תכונה קומבינטורית לא טריוויאלית. חשבו על טבלה שבה השורות מיוצגות על ידי הערכים האפשריים של {% equation %}x{% endequation %} והעמודות על פי הערכים האפשריים של {% equation %}y{% endequation %} ובתא בטבלה המתאים לזוג {% equation %}\left(x,y\right){% endequation %} כלשהו יש ביט המתאים לפלט הפרוטוקול עבור {% equation %}\left(x,y\right){% endequation %}. אז הטבלה ניתנת לחלוקה ל<strong>מלבנים כרומטיים</strong> - כלומר, מלבנים שכל אחד מהם בנפרד, או שכולו מסומן ב-0-ים, או שכולו מסומן ב-1-ים.

צריך להיות קצת זהירים עם השימוש במילה "מלבן" כאן, כי הכוונה אינה למלבן גאומטרי אלא להכללה שלו - מלבן קומבינטורי. במלבן גאומטרי כל השורות סמוכות זו לזו, אבל כאן זה לא הכרחי. פורמלית, אם יש לנו שתי קבוצות {% equation %}X,Y{% endequation %} (חשבו עליהם כעל אוספי כל ה-{% equation %}x{% endequation %}-ים וה-{% equation %}y{% endequation %}-ים האפשריים) ויש לנו שתי תת קבוצות {% equation %}A\subseteq X{% endequation %} ו-{% equation %}B\subseteq Y{% endequation %}, אז {% equation %}A\times B{% endequation %} היא מלבן קומבינטורי, גם אם אברי {% equation %}A{% endequation %} או {% equation %}B{% endequation %} לא באים באופן רציף. הגדרה שקולה למלבן קומבינטורי הוא זו: קבוצה של זוגות {% equation %}\left(x,y\right){% endequation %} כך שאם {% equation %}\left(x_{1},y_{1}\right),\left(x_{2},y_{2}\right){% endequation %} שייכים לקבוצה, כך גם {% equation %}\left(x_{1},y_{2}\right){% endequation %} ו-{% equation %}\left(x_{2},y_{1}\right){% endequation %}. נראה מוכר? זה בדיוק מה שהוכחו למעלה - שלכל צומת בפרוטקול, קבוצת "זוגות הקלטים שמביאות את אליס ובוב לצומת הזה" היא מלבן קומבינטורי.

נניח שלפרוטוקול יש {% equation %}t{% endequation %} עלים - כלומר, יש בדיוק {% equation %}t{% endequation %} מסלולים שונים מתחילת הפרוטוקול ועד סופו. כל עלה כזה מגדיר מלבן מונוכרומטי בתוך {% equation %}X\times Y{% endequation %}, ואיחוד כל המלבנים הללו הוא כל {% equation %}X\times Y{% endequation %}. לכן, אם נצליח להראות עבור {% equation %}f{% endequation %} כלשהי שבכל חלוקה אפשרית של {% equation %}X\times Y{% endequation %} למלבנים מונוכרומטיים (מונוכרומטיים ביחס ל-{% equation %}f{% endequation %}, כלומר בכל מלבן כזה {% equation %}f{% endequation %} נותנת את אותו ערך לכל אברי המלבן) יש <strong>לפחות</strong> {% equation %}t{% endequation %} מלבנים, הראינו שבעץ הפרוטקול חייבים להיות <strong>לפחות</strong> {% equation %}t{% endequation %} עלים. מכיוון שזהו עץ בינארי (לכל צומת יש בדיוק שני בנים), זה מניב חסם תחתון כלשהו על עומק העץ - הוא חייב להיות לפחות {% equation %}\lg t{% endequation %}. זה, בתורו, מניב חסם תחתון על סיבוכיות התקשורת של הפרוטוקול, כי עומק העץ הוא כמספר הביטים שמוחלפים במהלך ריצת הפרוטוקול.

סיכום: אם עבור {% equation %}f{% endequation %} נראה שכל נסיון לפרק את {% equation %}X\times Y{% endequation %} למלבנים מונוכרומטיים ביחס ל-{% equation %}f{% endequation %} דורש המון מלבנים, הראינו חסם תחתון גדול על סיבוכיות התקשורת של {% equation %}f{% endequation %}.

זה מוביל אותנו לשיטה האלמנטרית ביותר למציאת חסמים תחתונים - שיטת ה-Fooling Set. כשלמדתי את הקורס בנושא בדיחה ידועה הייתה למצוא תרגומים מגוחכים למונח הזה - "קבוצה היתולית" ו"קבוצה קרקסית" היו חלק מההצעות. לדעתי "קבוצה משטה" היא התרגום המתאים ביותר, ובו אשתמש. הרעיון בקבוצה משטה הוא פשוט - אם נצליח למצוא קבוצה של קלטים {% equation %}A{% endequation %} כך שלכל {% equation %}\left(x,y\right)\in A{% endequation %} מתקיים {% equation %}f\left(x,y\right)=1{% endequation %} (כאשר {% equation %}f{% endequation %} היא הפונקציה שאנו מנסים למצוא לה חסם תחתון) אבל לכל {% equation %}\left(x_{1},y_{1}\right),\left(x_{2},y_{2}\right)\in A{% endequation %} מתקיים ש-{% equation %}f\left(x_{1},y_{2}\right)=0{% endequation %} או {% equation %}f\left(x_{2},y_{1}\right)=0{% endequation %}, אז בהכרח כל זוג {% equation %}\left(x,y\right)\in A{% endequation %} חייב לשכון במלבן מונוכרומטי אחר, בכל חלוקה אפשרית של {% equation %}X\times Y{% endequation %} למלבנים מונוכרומטיים (כי אם {% equation %}\left(x_{1},y_{1}\right),\left(x_{2},y_{2}\right){% endequation %} שוכנים באותו המלבן, כך גם {% equation %}\left(x_{1},y_{2}\right){% endequation %} ו-{% equation %}\left(x_{2},y_{1}\right){% endequation %} ואחד מהם הוא בעל ה"צבע" הלא נכון). אותו הדבר עובד, כמובן, גם אם דורשים שכל אברי {% equation %}A{% endequation %} יחזירו 0. לכן בכל חלוקה של {% equation %}X\times Y{% endequation %} למלבנים מונוכרומטיים יש לפחות {% equation %}\left|A\right|{% endequation %} מלבנים ולכן {% equation %}\lg\left|A\right|{% endequation %} הוא חסם תחתון על סיבוכיות התקשורת של {% equation %}f{% endequation %}.

דוגמה? נניח ש-{% equation %}f{% endequation %} היא פונקצית השוויון: {% equation %}\mbox{EQ}\left(x,y\right)=1{% endequation %} אם ורק אם {% equation %}x=y{% endequation %}. אז {% equation %}A=\left\{ \left(x,y\right)|x=y\right\} {% endequation %} היא כמובן קבוצה משטה; מצד אחד {% equation %}f\left(x,y\right)=1{% endequation %} לכל {% equation %}\left(x,y\right)\in A{% endequation %}, ומצד שני {% equation %}f\left(x_{1},y_{2}\right)=0{% endequation %} כאשר {% equation %}x_{1}\ne y_{2}{% endequation %}. מה גודל {% equation %}A{% endequation %}? ובכן, האיברים מיוצגים בעזרת {% equation %}n{% endequation %} ביטים, ולכן יש {% equation %}2^{n}{% endequation %} ערכים אפשריים של {% equation %}x{% endequation %}, ולכן של איברים ל-{% equation %}A{% endequation %}, כלומר {% equation %}\left|A\right|=2^{n}{% endequation %}, כלומר החסם התחתון על סיבוכיות התקשורת שאותו מקבלים הוא {% equation %}\lg\left|A\right|=n{% endequation %} - וחסם תחתון של {% equation %}\Omega\left(n\right){% endequation %} הוא אופטימלי למדי בפונקציות שמחזירות רק ביט בודד (כי בוב יכול פשוט לשלוח לאליס את כל הביטים שלו ואליס תבצע את החישוב ותשלח לו בחזרה את ביט הפלט של {% equation %}f{% endequation %} כדי שגם הוא יידע). זה מראה מייד ש-{% equation %}\mbox{EQ}{% endequation %} היא מאותן פונקציות שהכרחי לשלוח את כל המידע כדי לחשב אותן במשותף. אותו תעלול מראה חסם תחתון של {% equation %}\Omega\left(n\right){% endequation %} גם על הפונקציה הבאה: אם {% equation %}A,B{% endequation %} הן שתי תת קבוצות של {% equation %}\left\{ 1,\dots,n\right\} {% endequation %}, אז {% equation %}f\left(A,B\right)=1{% endequation %} אם שתי הקבוצות נחתכות. במקרה זה הקבוצה המשטה היא אוסף כל הזוגות {% equation %}\left(A,\overline{A}\right){% endequation %} ({% equation %}\overline{A}{% endequation %} הוא המשלים של {% equation %}A{% endequation %} - כל האיברים האפשריים מהתחום שאינם ב-{% equation %}A{% endequation %}).

אם כן, זו הייתה טעימה ראשונית בלבד של מה זו סיבוכיות תקשורת, של מתי אפשר להתגבר על החסם הטריוויאלי ומתי אפשר להוכיח שהחסם הטריוויאלי הוא כל מה שיש. כמובן שכל זה היה רק קצה הקרחון; אני מקווה בעתיד לכתוב עוד פוסטים שיתארו דברים נחמדים שקשורים לנושא.