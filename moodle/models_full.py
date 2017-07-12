# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class MdlAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    alwaysshowdescription = models.SmallIntegerField()
    nosubmissions = models.SmallIntegerField()
    submissiondrafts = models.SmallIntegerField()
    sendnotifications = models.SmallIntegerField()
    sendlatenotifications = models.SmallIntegerField()
    duedate = models.BigIntegerField()
    allowsubmissionsfromdate = models.BigIntegerField()
    grade = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    requiresubmissionstatement = models.SmallIntegerField()
    completionsubmit = models.SmallIntegerField()
    cutoffdate = models.BigIntegerField()
    teamsubmission = models.SmallIntegerField()
    requireallteammemberssubmit = models.SmallIntegerField()
    teamsubmissiongroupingid = models.BigIntegerField()
    blindmarking = models.SmallIntegerField()
    revealidentities = models.SmallIntegerField()
    attemptreopenmethod = models.CharField(max_length=10)
    maxattempts = models.IntegerField()
    markingworkflow = models.SmallIntegerField()
    markingallocation = models.SmallIntegerField()
    sendstudentnotifications = models.SmallIntegerField()
    preventsubmissionnotingroup = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assign'


class MdlAssignGrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    grader = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    attemptnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assign_grades'
        unique_together = (('assignment', 'userid', 'attemptnumber'),)


class MdlAssignOverrides(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignid = models.BigIntegerField()
    groupid = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    sortorder = models.BigIntegerField(blank=True, null=True)
    allowsubmissionsfromdate = models.BigIntegerField(blank=True, null=True)
    duedate = models.BigIntegerField(blank=True, null=True)
    cutoffdate = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_assign_overrides'


class MdlAssignPluginConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    plugin = models.CharField(max_length=28)
    subtype = models.CharField(max_length=28)
    name = models.CharField(max_length=28)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_assign_plugin_config'


class MdlAssignSubmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    status = models.CharField(max_length=10, blank=True, null=True)
    groupid = models.BigIntegerField()
    attemptnumber = models.BigIntegerField()
    latest = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assign_submission'
        unique_together = (('assignment', 'userid', 'groupid', 'attemptnumber'),)


class MdlAssignUserFlags(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    assignment = models.BigIntegerField()
    locked = models.BigIntegerField()
    mailed = models.SmallIntegerField()
    extensionduedate = models.BigIntegerField()
    workflowstate = models.CharField(max_length=20, blank=True, null=True)
    allocatedmarker = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assign_user_flags'


class MdlAssignUserMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assign_user_mapping'


class MdlAssignfeedbackComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    grade = models.BigIntegerField()
    commenttext = models.TextField(blank=True, null=True)
    commentformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assignfeedback_comments'


class MdlAssignfeedbackEditpdfAnnot(models.Model):
    id = models.BigAutoField(primary_key=True)
    gradeid = models.BigIntegerField()
    pageno = models.BigIntegerField()
    x = models.BigIntegerField(blank=True, null=True)
    y = models.BigIntegerField(blank=True, null=True)
    endx = models.BigIntegerField(blank=True, null=True)
    endy = models.BigIntegerField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    colour = models.CharField(max_length=10, blank=True, null=True)
    draft = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assignfeedback_editpdf_annot'


class MdlAssignfeedbackEditpdfCmnt(models.Model):
    id = models.BigAutoField(primary_key=True)
    gradeid = models.BigIntegerField()
    x = models.BigIntegerField(blank=True, null=True)
    y = models.BigIntegerField(blank=True, null=True)
    width = models.BigIntegerField(blank=True, null=True)
    rawtext = models.TextField(blank=True, null=True)
    pageno = models.BigIntegerField()
    colour = models.CharField(max_length=10, blank=True, null=True)
    draft = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assignfeedback_editpdf_cmnt'


class MdlAssignfeedbackEditpdfQueue(models.Model):
    id = models.BigAutoField(primary_key=True)
    submissionid = models.BigIntegerField()
    submissionattempt = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assignfeedback_editpdf_queue'


class MdlAssignfeedbackEditpdfQuick(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    rawtext = models.TextField()
    width = models.BigIntegerField()
    colour = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_assignfeedback_editpdf_quick'


class MdlAssignfeedbackFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    grade = models.BigIntegerField()
    numfiles = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assignfeedback_file'


class MdlAssignment(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    assignmenttype = models.CharField(max_length=50)
    resubmit = models.SmallIntegerField()
    preventlate = models.SmallIntegerField()
    emailteachers = models.SmallIntegerField()
    var1 = models.BigIntegerField(blank=True, null=True)
    var2 = models.BigIntegerField(blank=True, null=True)
    var3 = models.BigIntegerField(blank=True, null=True)
    var4 = models.BigIntegerField(blank=True, null=True)
    var5 = models.BigIntegerField(blank=True, null=True)
    maxbytes = models.BigIntegerField()
    timedue = models.BigIntegerField()
    timeavailable = models.BigIntegerField()
    grade = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assignment'


class MdlAssignmentSubmissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    numfiles = models.BigIntegerField()
    data1 = models.TextField(blank=True, null=True)
    data2 = models.TextField(blank=True, null=True)
    grade = models.BigIntegerField()
    submissioncomment = models.TextField()
    format = models.SmallIntegerField()
    teacher = models.BigIntegerField()
    timemarked = models.BigIntegerField()
    mailed = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assignment_submissions'


class MdlAssignmentUpgrade(models.Model):
    id = models.BigAutoField(primary_key=True)
    oldcmid = models.BigIntegerField()
    oldinstance = models.BigIntegerField()
    newcmid = models.BigIntegerField()
    newinstance = models.BigIntegerField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assignment_upgrade'


class MdlAssignsubmissionFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    submission = models.BigIntegerField()
    numfiles = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assignsubmission_file'


class MdlAssignsubmissionOnlinetext(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    submission = models.BigIntegerField()
    onlinetext = models.TextField(blank=True, null=True)
    onlineformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_assignsubmission_onlinetext'


class MdlBackupControllers(models.Model):
    id = models.BigAutoField(primary_key=True)
    backupid = models.CharField(unique=True, max_length=32)
    operation = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    itemid = models.BigIntegerField()
    format = models.CharField(max_length=20)
    interactive = models.SmallIntegerField()
    purpose = models.SmallIntegerField()
    userid = models.BigIntegerField()
    status = models.SmallIntegerField()
    execution = models.SmallIntegerField()
    executiontime = models.BigIntegerField()
    checksum = models.CharField(max_length=32)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    controller = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_backup_controllers'


class MdlBackupCourses(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField(unique=True)
    laststarttime = models.BigIntegerField()
    lastendtime = models.BigIntegerField()
    laststatus = models.CharField(max_length=1)
    nextstarttime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_backup_courses'


class MdlBackupLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    backupid = models.CharField(max_length=32)
    loglevel = models.SmallIntegerField()
    message = models.TextField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_backup_logs'
        unique_together = (('backupid', 'id'),)


class MdlBadge(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usercreated = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    issuername = models.CharField(max_length=255)
    issuerurl = models.CharField(max_length=255)
    issuercontact = models.CharField(max_length=255, blank=True, null=True)
    expiredate = models.BigIntegerField(blank=True, null=True)
    expireperiod = models.BigIntegerField(blank=True, null=True)
    type = models.SmallIntegerField()
    courseid = models.BigIntegerField(blank=True, null=True)
    message = models.TextField()
    messagesubject = models.TextField()
    attachment = models.SmallIntegerField()
    notification = models.SmallIntegerField()
    status = models.SmallIntegerField()
    nextcron = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_badge'


class MdlBadgeBackpack(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    email = models.CharField(max_length=100)
    backpackurl = models.CharField(max_length=255)
    backpackuid = models.BigIntegerField()
    autosync = models.SmallIntegerField()
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_badge_backpack'


class MdlBadgeCriteria(models.Model):
    id = models.BigAutoField(primary_key=True)
    badgeid = models.BigIntegerField()
    criteriatype = models.BigIntegerField(blank=True, null=True)
    method = models.SmallIntegerField()
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_badge_criteria'
        unique_together = (('badgeid', 'criteriatype'),)


class MdlBadgeCriteriaMet(models.Model):
    id = models.BigAutoField(primary_key=True)
    issuedid = models.BigIntegerField(blank=True, null=True)
    critid = models.BigIntegerField()
    userid = models.BigIntegerField()
    datemet = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_badge_criteria_met'


class MdlBadgeCriteriaParam(models.Model):
    id = models.BigAutoField(primary_key=True)
    critid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_badge_criteria_param'


class MdlBadgeExternal(models.Model):
    id = models.BigAutoField(primary_key=True)
    backpackid = models.BigIntegerField()
    collectionid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_badge_external'


class MdlBadgeIssued(models.Model):
    id = models.BigAutoField(primary_key=True)
    badgeid = models.BigIntegerField()
    userid = models.BigIntegerField()
    uniquehash = models.TextField()
    dateissued = models.BigIntegerField()
    dateexpire = models.BigIntegerField(blank=True, null=True)
    visible = models.SmallIntegerField()
    issuernotified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_badge_issued'
        unique_together = (('badgeid', 'userid'),)


class MdlBadgeManualAward(models.Model):
    id = models.BigAutoField(primary_key=True)
    badgeid = models.BigIntegerField()
    recipientid = models.BigIntegerField()
    issuerid = models.BigIntegerField()
    issuerrole = models.BigIntegerField()
    datemet = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_badge_manual_award'


class MdlBlock(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=40)
    cron = models.BigIntegerField()
    lastcron = models.BigIntegerField()
    visible = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_block'


class MdlBlockCommunity(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    coursename = models.CharField(max_length=255)
    coursedescription = models.TextField(blank=True, null=True)
    courseurl = models.CharField(max_length=255)
    imageurl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_block_community'


class MdlBlockInstances(models.Model):
    id = models.BigAutoField(primary_key=True)
    blockname = models.CharField(max_length=40)
    parentcontextid = models.BigIntegerField()
    showinsubcontexts = models.SmallIntegerField()
    requiredbytheme = models.SmallIntegerField()
    pagetypepattern = models.CharField(max_length=64)
    subpagepattern = models.CharField(max_length=16, blank=True, null=True)
    defaultregion = models.CharField(max_length=16)
    defaultweight = models.BigIntegerField()
    configdata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_block_instances'


class MdlBlockPositions(models.Model):
    id = models.BigAutoField(primary_key=True)
    blockinstanceid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    pagetype = models.CharField(max_length=64)
    subpage = models.CharField(max_length=16)
    visible = models.SmallIntegerField()
    region = models.CharField(max_length=16)
    weight = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_block_positions'
        unique_together = (('blockinstanceid', 'contextid', 'pagetype', 'subpage'),)


class MdlBlockRecentActivity(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    cmid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    userid = models.BigIntegerField()
    action = models.SmallIntegerField()
    modname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_block_recent_activity'


class MdlBlockRssClient(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    title = models.TextField()
    preferredtitle = models.CharField(max_length=64)
    description = models.TextField()
    shared = models.SmallIntegerField()
    url = models.CharField(max_length=255)
    skiptime = models.BigIntegerField()
    skipuntil = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_block_rss_client'


class MdlBlogAssociation(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    blogid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_blog_association'


class MdlBlogExternal(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.TextField()
    filtertags = models.CharField(max_length=255, blank=True, null=True)
    failedlastsync = models.SmallIntegerField()
    timemodified = models.BigIntegerField(blank=True, null=True)
    timefetched = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_blog_external'


class MdlBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    numbering = models.SmallIntegerField()
    navstyle = models.SmallIntegerField()
    customtitles = models.SmallIntegerField()
    revision = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_book'


class MdlBookChapters(models.Model):
    id = models.BigAutoField(primary_key=True)
    bookid = models.BigIntegerField()
    pagenum = models.BigIntegerField()
    subchapter = models.BigIntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    contentformat = models.SmallIntegerField()
    hidden = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    importsrc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_book_chapters'


class MdlCacheFilters(models.Model):
    id = models.BigAutoField(primary_key=True)
    filter = models.CharField(max_length=32)
    version = models.BigIntegerField()
    md5key = models.CharField(max_length=32)
    rawtext = models.TextField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_cache_filters'


class MdlCacheFlags(models.Model):
    id = models.BigAutoField(primary_key=True)
    flagtype = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    timemodified = models.BigIntegerField()
    value = models.TextField()
    expiry = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_cache_flags'


class MdlCapabilities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    captype = models.CharField(max_length=50)
    contextlevel = models.BigIntegerField()
    component = models.CharField(max_length=100)
    riskbitmask = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_capabilities'


class MdlChat(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    keepdays = models.BigIntegerField()
    studentlogs = models.SmallIntegerField()
    chattime = models.BigIntegerField()
    schedule = models.SmallIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_chat'


class MdlChatMessages(models.Model):
    id = models.BigAutoField(primary_key=True)
    chatid = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    system = models.SmallIntegerField()
    message = models.TextField()
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_chat_messages'


class MdlChatMessagesCurrent(models.Model):
    id = models.BigAutoField(primary_key=True)
    chatid = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    system = models.SmallIntegerField()
    message = models.TextField()
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_chat_messages_current'


class MdlChatUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    chatid = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    version = models.CharField(max_length=16)
    ip = models.CharField(max_length=45)
    firstping = models.BigIntegerField()
    lastping = models.BigIntegerField()
    lastmessageping = models.BigIntegerField()
    sid = models.CharField(max_length=32)
    course = models.BigIntegerField()
    lang = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mdl_chat_users'


class MdlChoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    publish = models.SmallIntegerField()
    showresults = models.SmallIntegerField()
    display = models.SmallIntegerField()
    allowupdate = models.SmallIntegerField()
    allowmultiple = models.SmallIntegerField()
    showunanswered = models.SmallIntegerField()
    includeinactive = models.SmallIntegerField()
    limitanswers = models.SmallIntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    showpreview = models.SmallIntegerField()
    timemodified = models.BigIntegerField()
    completionsubmit = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_choice'


class MdlChoiceAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    choiceid = models.BigIntegerField()
    userid = models.BigIntegerField()
    optionid = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_choice_answers'


class MdlChoiceOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    choiceid = models.BigIntegerField()
    text = models.TextField(blank=True, null=True)
    maxanswers = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_choice_options'


class MdlCohort(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    name = models.CharField(max_length=254)
    idnumber = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    visible = models.SmallIntegerField()
    component = models.CharField(max_length=100)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_cohort'


class MdlCohortMembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    cohortid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timeadded = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_cohort_members'
        unique_together = (('cohortid', 'userid'),)


class MdlComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=255, blank=True, null=True)
    commentarea = models.CharField(max_length=255)
    itemid = models.BigIntegerField()
    content = models.TextField()
    format = models.SmallIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_comments'


class MdlCompetency(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    idnumber = models.CharField(max_length=100, blank=True, null=True)
    competencyframeworkid = models.BigIntegerField()
    parentid = models.BigIntegerField()
    path = models.CharField(max_length=255)
    sortorder = models.BigIntegerField()
    ruletype = models.CharField(max_length=100, blank=True, null=True)
    ruleoutcome = models.SmallIntegerField()
    ruleconfig = models.TextField(blank=True, null=True)
    scaleid = models.BigIntegerField(blank=True, null=True)
    scaleconfiguration = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_competency'
        unique_together = (('competencyframeworkid', 'idnumber'),)


class MdlCompetencyCoursecomp(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    competencyid = models.BigIntegerField()
    ruleoutcome = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_coursecomp'
        unique_together = (('courseid', 'competencyid'),)


class MdlCompetencyCoursecompsetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField(unique=True)
    pushratingstouserplans = models.SmallIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_competency_coursecompsetting'


class MdlCompetencyEvidence(models.Model):
    id = models.BigAutoField(primary_key=True)
    usercompetencyid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    action = models.SmallIntegerField()
    actionuserid = models.BigIntegerField(blank=True, null=True)
    descidentifier = models.CharField(max_length=255)
    desccomponent = models.CharField(max_length=255)
    desca = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    grade = models.BigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_evidence'


class MdlCompetencyFramework(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(max_length=100, blank=True, null=True)
    contextid = models.BigIntegerField()
    idnumber = models.CharField(unique=True, max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    scaleid = models.BigIntegerField(blank=True, null=True)
    scaleconfiguration = models.TextField()
    visible = models.SmallIntegerField()
    taxonomies = models.CharField(max_length=255)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_competency_framework'


class MdlCompetencyModulecomp(models.Model):
    id = models.BigAutoField(primary_key=True)
    cmid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    competencyid = models.BigIntegerField()
    ruleoutcome = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_modulecomp'
        unique_together = (('cmid', 'competencyid'),)


class MdlCompetencyPlan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    userid = models.BigIntegerField()
    templateid = models.BigIntegerField(blank=True, null=True)
    origtemplateid = models.BigIntegerField(blank=True, null=True)
    status = models.SmallIntegerField()
    duedate = models.BigIntegerField(blank=True, null=True)
    reviewerid = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_plan'


class MdlCompetencyPlancomp(models.Model):
    id = models.BigAutoField(primary_key=True)
    planid = models.BigIntegerField()
    competencyid = models.BigIntegerField()
    sortorder = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_plancomp'
        unique_together = (('planid', 'competencyid'),)


class MdlCompetencyRelatedcomp(models.Model):
    id = models.BigAutoField(primary_key=True)
    competencyid = models.BigIntegerField()
    relatedcompetencyid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_relatedcomp'


class MdlCompetencyTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(max_length=100, blank=True, null=True)
    contextid = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    visible = models.SmallIntegerField()
    duedate = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_competency_template'


class MdlCompetencyTemplatecohort(models.Model):
    id = models.BigAutoField(primary_key=True)
    templateid = models.BigIntegerField()
    cohortid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_templatecohort'
        unique_together = (('templateid', 'cohortid'),)


class MdlCompetencyTemplatecomp(models.Model):
    id = models.BigAutoField(primary_key=True)
    templateid = models.BigIntegerField()
    competencyid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    sortorder = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_competency_templatecomp'


class MdlCompetencyUsercomp(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    competencyid = models.BigIntegerField()
    status = models.SmallIntegerField()
    reviewerid = models.BigIntegerField(blank=True, null=True)
    proficiency = models.SmallIntegerField(blank=True, null=True)
    grade = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_usercomp'
        unique_together = (('userid', 'competencyid'),)


class MdlCompetencyUsercompcourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    competencyid = models.BigIntegerField()
    proficiency = models.SmallIntegerField(blank=True, null=True)
    grade = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_usercompcourse'
        unique_together = (('userid', 'courseid', 'competencyid'),)


class MdlCompetencyUsercompplan(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    competencyid = models.BigIntegerField()
    planid = models.BigIntegerField()
    proficiency = models.SmallIntegerField(blank=True, null=True)
    grade = models.BigIntegerField(blank=True, null=True)
    sortorder = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_usercompplan'
        unique_together = (('userid', 'competencyid', 'planid'),)


class MdlCompetencyUserevidence(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    descriptionformat = models.SmallIntegerField()
    url = models.TextField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_userevidence'


class MdlCompetencyUserevidencecomp(models.Model):
    id = models.BigAutoField(primary_key=True)
    userevidenceid = models.BigIntegerField()
    competencyid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_competency_userevidencecomp'
        unique_together = (('userevidenceid', 'competencyid'),)


class MdlConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_config'


class MdlConfigLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    plugin = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    value = models.TextField(blank=True, null=True)
    oldvalue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_config_log'


class MdlConfigPlugins(models.Model):
    id = models.BigAutoField(primary_key=True)
    plugin = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_config_plugins'
        unique_together = (('plugin', 'name'),)


class MdlContext(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextlevel = models.BigIntegerField()
    instanceid = models.BigIntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)
    depth = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_context'
        unique_together = (('contextlevel', 'instanceid'),)


class MdlContextTemp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    path = models.CharField(max_length=255)
    depth = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_context_temp'


class MdlCourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)
    summaryformat = models.SmallIntegerField()
    format = models.CharField(max_length=21)
    showgrades = models.SmallIntegerField()
    newsitems = models.IntegerField()
    startdate = models.BigIntegerField()
    enddate = models.BigIntegerField()
    marker = models.BigIntegerField()
    maxbytes = models.BigIntegerField()
    legacyfiles = models.SmallIntegerField()
    showreports = models.SmallIntegerField()
    visible = models.SmallIntegerField()
    visibleold = models.SmallIntegerField()
    groupmode = models.SmallIntegerField()
    groupmodeforce = models.SmallIntegerField()
    defaultgroupingid = models.BigIntegerField()
    lang = models.CharField(max_length=30)
    calendartype = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    requested = models.SmallIntegerField()
    enablecompletion = models.SmallIntegerField()
    completionnotify = models.SmallIntegerField()
    cacherev = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_course'


class MdlCourseCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    parent = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    coursecount = models.BigIntegerField()
    visible = models.SmallIntegerField()
    visibleold = models.SmallIntegerField()
    timemodified = models.BigIntegerField()
    depth = models.BigIntegerField()
    path = models.CharField(max_length=255)
    theme = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_course_categories'


class MdlCourseCompletionAggrMethd(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    criteriatype = models.BigIntegerField(blank=True, null=True)
    method = models.SmallIntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_course_completion_aggr_methd'
        unique_together = (('course', 'criteriatype'),)


class MdlCourseCompletionCritCompl(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    course = models.BigIntegerField()
    criteriaid = models.BigIntegerField()
    gradefinal = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    unenroled = models.BigIntegerField(blank=True, null=True)
    timecompleted = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_course_completion_crit_compl'
        unique_together = (('userid', 'course', 'criteriaid'),)


class MdlCourseCompletionCriteria(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    criteriatype = models.BigIntegerField()
    module = models.CharField(max_length=100, blank=True, null=True)
    moduleinstance = models.BigIntegerField(blank=True, null=True)
    courseinstance = models.BigIntegerField(blank=True, null=True)
    enrolperiod = models.BigIntegerField(blank=True, null=True)
    timeend = models.BigIntegerField(blank=True, null=True)
    gradepass = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    role = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_course_completion_criteria'


class MdlCourseCompletions(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    course = models.BigIntegerField()
    timeenrolled = models.BigIntegerField()
    timestarted = models.BigIntegerField()
    timecompleted = models.BigIntegerField(blank=True, null=True)
    reaggregate = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_course_completions'
        unique_together = (('userid', 'course'),)


class MdlCourseFormatOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    format = models.CharField(max_length=21)
    sectionid = models.BigIntegerField()
    name = models.CharField(max_length=100)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_course_format_options'
        unique_together = (('courseid', 'format', 'sectionid', 'name'),)


class MdlCourseModules(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    module = models.BigIntegerField()
    instance = models.BigIntegerField()
    section = models.BigIntegerField()
    idnumber = models.CharField(max_length=100, blank=True, null=True)
    added = models.BigIntegerField()
    score = models.SmallIntegerField()
    indent = models.IntegerField()
    visible = models.SmallIntegerField()
    visibleold = models.SmallIntegerField()
    groupmode = models.SmallIntegerField()
    groupingid = models.BigIntegerField()
    completion = models.SmallIntegerField()
    completiongradeitemnumber = models.BigIntegerField(blank=True, null=True)
    completionview = models.SmallIntegerField()
    completionexpected = models.BigIntegerField()
    showdescription = models.SmallIntegerField()
    availability = models.TextField(blank=True, null=True)
    deletioninprogress = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_course_modules'


class MdlCourseModulesCompletion(models.Model):
    id = models.BigAutoField(primary_key=True)
    coursemoduleid = models.BigIntegerField()
    userid = models.BigIntegerField()
    completionstate = models.SmallIntegerField()
    viewed = models.SmallIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_course_modules_completion'
        unique_together = (('userid', 'coursemoduleid'),)


class MdlCoursePublished(models.Model):
    id = models.BigAutoField(primary_key=True)
    huburl = models.CharField(max_length=255, blank=True, null=True)
    courseid = models.BigIntegerField()
    timepublished = models.BigIntegerField()
    enrollable = models.SmallIntegerField()
    hubcourseid = models.BigIntegerField()
    status = models.SmallIntegerField(blank=True, null=True)
    timechecked = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_course_published'


class MdlCourseRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=100)
    summary = models.TextField()
    summaryformat = models.SmallIntegerField()
    category = models.BigIntegerField()
    reason = models.TextField()
    requester = models.BigIntegerField()
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mdl_course_request'


class MdlCourseSections(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    section = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    summaryformat = models.SmallIntegerField()
    sequence = models.TextField(blank=True, null=True)
    visible = models.SmallIntegerField()
    availability = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_course_sections'
        unique_together = (('course', 'section'),)


class MdlData(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    comments = models.SmallIntegerField()
    timeavailablefrom = models.BigIntegerField()
    timeavailableto = models.BigIntegerField()
    timeviewfrom = models.BigIntegerField()
    timeviewto = models.BigIntegerField()
    requiredentries = models.IntegerField()
    requiredentriestoview = models.IntegerField()
    maxentries = models.IntegerField()
    rssarticles = models.SmallIntegerField()
    singletemplate = models.TextField(blank=True, null=True)
    listtemplate = models.TextField(blank=True, null=True)
    listtemplateheader = models.TextField(blank=True, null=True)
    listtemplatefooter = models.TextField(blank=True, null=True)
    addtemplate = models.TextField(blank=True, null=True)
    rsstemplate = models.TextField(blank=True, null=True)
    rsstitletemplate = models.TextField(blank=True, null=True)
    csstemplate = models.TextField(blank=True, null=True)
    jstemplate = models.TextField(blank=True, null=True)
    asearchtemplate = models.TextField(blank=True, null=True)
    approval = models.SmallIntegerField()
    manageapproved = models.SmallIntegerField()
    scale = models.BigIntegerField()
    assessed = models.BigIntegerField()
    assesstimestart = models.BigIntegerField()
    assesstimefinish = models.BigIntegerField()
    defaultsort = models.BigIntegerField()
    defaultsortdir = models.SmallIntegerField()
    editany = models.SmallIntegerField()
    notification = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    config = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_data'


class MdlDataContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    fieldid = models.BigIntegerField()
    recordid = models.BigIntegerField()
    content = models.TextField(blank=True, null=True)
    content1 = models.TextField(blank=True, null=True)
    content2 = models.TextField(blank=True, null=True)
    content3 = models.TextField(blank=True, null=True)
    content4 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_data_content'


class MdlDataFields(models.Model):
    id = models.BigAutoField(primary_key=True)
    dataid = models.BigIntegerField()
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    required = models.SmallIntegerField()
    param1 = models.TextField(blank=True, null=True)
    param2 = models.TextField(blank=True, null=True)
    param3 = models.TextField(blank=True, null=True)
    param4 = models.TextField(blank=True, null=True)
    param5 = models.TextField(blank=True, null=True)
    param6 = models.TextField(blank=True, null=True)
    param7 = models.TextField(blank=True, null=True)
    param8 = models.TextField(blank=True, null=True)
    param9 = models.TextField(blank=True, null=True)
    param10 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_data_fields'


class MdlDataRecords(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    dataid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    approved = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_data_records'


class MdlEditorAttoAutosave(models.Model):
    id = models.BigAutoField(primary_key=True)
    elementid = models.CharField(max_length=255)
    contextid = models.BigIntegerField()
    pagehash = models.CharField(max_length=64)
    userid = models.BigIntegerField()
    drafttext = models.TextField()
    draftid = models.BigIntegerField(blank=True, null=True)
    pageinstance = models.CharField(max_length=64)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_editor_atto_autosave'
        unique_together = (('elementid', 'contextid', 'userid', 'pagehash'),)


class MdlEnrol(models.Model):
    id = models.BigAutoField(primary_key=True)
    enrol = models.CharField(max_length=20)
    status = models.BigIntegerField()
    courseid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    enrolperiod = models.BigIntegerField(blank=True, null=True)
    enrolstartdate = models.BigIntegerField(blank=True, null=True)
    enrolenddate = models.BigIntegerField(blank=True, null=True)
    expirynotify = models.SmallIntegerField(blank=True, null=True)
    expirythreshold = models.BigIntegerField(blank=True, null=True)
    notifyall = models.SmallIntegerField(blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    cost = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    roleid = models.BigIntegerField(blank=True, null=True)
    customint1 = models.BigIntegerField(blank=True, null=True)
    customint2 = models.BigIntegerField(blank=True, null=True)
    customint3 = models.BigIntegerField(blank=True, null=True)
    customint4 = models.BigIntegerField(blank=True, null=True)
    customint5 = models.BigIntegerField(blank=True, null=True)
    customint6 = models.BigIntegerField(blank=True, null=True)
    customint7 = models.BigIntegerField(blank=True, null=True)
    customint8 = models.BigIntegerField(blank=True, null=True)
    customchar1 = models.CharField(max_length=255, blank=True, null=True)
    customchar2 = models.CharField(max_length=255, blank=True, null=True)
    customchar3 = models.CharField(max_length=1333, blank=True, null=True)
    customdec1 = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    customdec2 = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    customtext1 = models.TextField(blank=True, null=True)
    customtext2 = models.TextField(blank=True, null=True)
    customtext3 = models.TextField(blank=True, null=True)
    customtext4 = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol'


class MdlEnrolFlatfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.CharField(max_length=30)
    roleid = models.BigIntegerField()
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_flatfile'


class MdlEnrolLtiLti2Consumer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    consumerkey256 = models.CharField(unique=True, max_length=255)
    consumerkey = models.TextField(blank=True, null=True)
    secret = models.CharField(max_length=1024)
    ltiversion = models.CharField(max_length=10, blank=True, null=True)
    consumername = models.CharField(max_length=255, blank=True, null=True)
    consumerversion = models.CharField(max_length=255, blank=True, null=True)
    consumerguid = models.CharField(max_length=1024, blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    toolproxy = models.TextField(blank=True, null=True)
    settings = models.TextField(blank=True, null=True)
    protected = models.SmallIntegerField()
    enabled = models.SmallIntegerField()
    enablefrom = models.BigIntegerField(blank=True, null=True)
    enableuntil = models.BigIntegerField(blank=True, null=True)
    lastaccess = models.BigIntegerField(blank=True, null=True)
    created = models.BigIntegerField()
    updated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_lti_lti2_consumer'


class MdlEnrolLtiLti2Context(models.Model):
    id = models.BigAutoField(primary_key=True)
    consumerid = models.BigIntegerField()
    lticontextkey = models.CharField(max_length=255)
    type = models.CharField(max_length=100, blank=True, null=True)
    settings = models.TextField(blank=True, null=True)
    created = models.BigIntegerField()
    updated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_lti_lti2_context'


class MdlEnrolLtiLti2Nonce(models.Model):
    id = models.BigAutoField(primary_key=True)
    consumerid = models.BigIntegerField()
    value = models.CharField(max_length=64)
    expires = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_lti_lti2_nonce'


class MdlEnrolLtiLti2ResourceLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField(blank=True, null=True)
    consumerid = models.BigIntegerField(blank=True, null=True)
    ltiresourcelinkkey = models.CharField(max_length=255)
    settings = models.TextField(blank=True, null=True)
    primaryresourcelinkid = models.BigIntegerField(blank=True, null=True)
    shareapproved = models.SmallIntegerField(blank=True, null=True)
    created = models.BigIntegerField()
    updated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_lti_lti2_resource_link'


class MdlEnrolLtiLti2ShareKey(models.Model):
    id = models.BigAutoField(primary_key=True)
    sharekey = models.CharField(unique=True, max_length=32)
    resourcelinkid = models.BigIntegerField(unique=True)
    autoapprove = models.SmallIntegerField()
    expires = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_lti_lti2_share_key'


class MdlEnrolLtiLti2ToolProxy(models.Model):
    id = models.BigAutoField(primary_key=True)
    toolproxykey = models.CharField(unique=True, max_length=32)
    consumerid = models.BigIntegerField()
    toolproxy = models.TextField()
    created = models.BigIntegerField()
    updated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_lti_lti2_tool_proxy'


class MdlEnrolLtiLti2UserResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    resourcelinkid = models.BigIntegerField()
    ltiuserkey = models.CharField(max_length=255)
    ltiresultsourcedid = models.CharField(max_length=1024)
    created = models.BigIntegerField()
    updated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_lti_lti2_user_result'


class MdlEnrolLtiToolConsumerMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    toolid = models.BigIntegerField()
    consumerid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_lti_tool_consumer_map'


class MdlEnrolLtiTools(models.Model):
    id = models.BigAutoField(primary_key=True)
    enrolid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    institution = models.CharField(max_length=40)
    lang = models.CharField(max_length=30)
    timezone = models.CharField(max_length=100)
    maxenrolled = models.BigIntegerField()
    maildisplay = models.SmallIntegerField()
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=2)
    gradesync = models.SmallIntegerField()
    gradesynccompletion = models.SmallIntegerField()
    membersync = models.SmallIntegerField()
    membersyncmode = models.SmallIntegerField()
    roleinstructor = models.BigIntegerField()
    rolelearner = models.BigIntegerField()
    secret = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_lti_tools'


class MdlEnrolLtiUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    toolid = models.BigIntegerField()
    serviceurl = models.TextField(blank=True, null=True)
    sourceid = models.TextField(blank=True, null=True)
    consumerkey = models.TextField(blank=True, null=True)
    consumersecret = models.TextField(blank=True, null=True)
    membershipsurl = models.TextField(blank=True, null=True)
    membershipsid = models.TextField(blank=True, null=True)
    lastgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    lastaccess = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_enrol_lti_users'


class MdlEnrolPaypal(models.Model):
    id = models.BigAutoField(primary_key=True)
    business = models.CharField(max_length=255)
    receiver_email = models.CharField(max_length=255)
    receiver_id = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    instanceid = models.BigIntegerField()
    memo = models.CharField(max_length=255)
    tax = models.CharField(max_length=255)
    option_name1 = models.CharField(max_length=255)
    option_selection1_x = models.CharField(max_length=255)
    option_name2 = models.CharField(max_length=255)
    option_selection2_x = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    pending_reason = models.CharField(max_length=255)
    reason_code = models.CharField(max_length=30)
    txn_id = models.CharField(max_length=255)
    parent_txn_id = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=30)
    timeupdated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_paypal'


class MdlEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    format = models.SmallIntegerField()
    courseid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()
    repeatid = models.BigIntegerField()
    modulename = models.CharField(max_length=20)
    instance = models.BigIntegerField()
    eventtype = models.CharField(max_length=20)
    timestart = models.BigIntegerField()
    timeduration = models.BigIntegerField()
    visible = models.SmallIntegerField()
    uuid = models.CharField(max_length=255)
    sequence = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    subscriptionid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_event'


class MdlEventSubscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255)
    courseid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()
    eventtype = models.CharField(max_length=20)
    pollinterval = models.BigIntegerField()
    lastupdated = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_event_subscriptions'


class MdlEventsHandlers(models.Model):
    id = models.BigAutoField(primary_key=True)
    eventname = models.CharField(max_length=166)
    component = models.CharField(max_length=166)
    handlerfile = models.CharField(max_length=255)
    handlerfunction = models.TextField(blank=True, null=True)
    schedule = models.CharField(max_length=255, blank=True, null=True)
    status = models.BigIntegerField()
    internal = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_events_handlers'
        unique_together = (('eventname', 'component'),)


class MdlEventsQueue(models.Model):
    id = models.BigAutoField(primary_key=True)
    eventdata = models.TextField()
    stackdump = models.TextField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_events_queue'


class MdlEventsQueueHandlers(models.Model):
    id = models.BigAutoField(primary_key=True)
    queuedeventid = models.BigIntegerField()
    handlerid = models.BigIntegerField()
    status = models.BigIntegerField(blank=True, null=True)
    errormessage = models.TextField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_events_queue_handlers'


class MdlExternalFunctions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    classname = models.CharField(max_length=100)
    methodname = models.CharField(max_length=100)
    classpath = models.CharField(max_length=255, blank=True, null=True)
    component = models.CharField(max_length=100)
    capabilities = models.CharField(max_length=255, blank=True, null=True)
    services = models.CharField(max_length=1333, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_external_functions'


class MdlExternalServices(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    enabled = models.SmallIntegerField()
    requiredcapability = models.CharField(max_length=150, blank=True, null=True)
    restrictedusers = models.SmallIntegerField()
    component = models.CharField(max_length=100, blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    downloadfiles = models.SmallIntegerField()
    uploadfiles = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_external_services'


class MdlExternalServicesFunctions(models.Model):
    id = models.BigAutoField(primary_key=True)
    externalserviceid = models.BigIntegerField()
    functionname = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'mdl_external_services_functions'


class MdlExternalServicesUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    externalserviceid = models.BigIntegerField()
    userid = models.BigIntegerField()
    iprestriction = models.CharField(max_length=255, blank=True, null=True)
    validuntil = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_external_services_users'


class MdlExternalTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=128)
    privatetoken = models.CharField(max_length=64, blank=True, null=True)
    tokentype = models.SmallIntegerField()
    userid = models.BigIntegerField()
    externalserviceid = models.BigIntegerField()
    sid = models.CharField(max_length=128, blank=True, null=True)
    contextid = models.BigIntegerField()
    creatorid = models.BigIntegerField()
    iprestriction = models.CharField(max_length=255, blank=True, null=True)
    validuntil = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    lastaccess = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_external_tokens'


class MdlFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    anonymous = models.SmallIntegerField()
    email_notification = models.SmallIntegerField()
    multiple_submit = models.SmallIntegerField()
    autonumbering = models.SmallIntegerField()
    site_after_submit = models.CharField(max_length=255)
    page_after_submit = models.TextField()
    page_after_submitformat = models.SmallIntegerField()
    publish_stats = models.SmallIntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionsubmit = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_feedback'


class MdlFeedbackCompleted(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedback = models.BigIntegerField()
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    random_response = models.BigIntegerField()
    anonymous_response = models.SmallIntegerField()
    courseid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_feedback_completed'


class MdlFeedbackCompletedtmp(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedback = models.BigIntegerField()
    userid = models.BigIntegerField()
    guestid = models.CharField(max_length=255)
    timemodified = models.BigIntegerField()
    random_response = models.BigIntegerField()
    anonymous_response = models.SmallIntegerField()
    courseid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_feedback_completedtmp'


class MdlFeedbackItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedback = models.BigIntegerField()
    template = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    presentation = models.TextField()
    typ = models.CharField(max_length=255)
    hasvalue = models.SmallIntegerField()
    position = models.SmallIntegerField()
    required = models.SmallIntegerField()
    dependitem = models.BigIntegerField()
    dependvalue = models.CharField(max_length=255)
    options = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_feedback_item'


class MdlFeedbackSitecourseMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedbackid = models.BigIntegerField()
    courseid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_feedback_sitecourse_map'


class MdlFeedbackTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    ispublic = models.SmallIntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_feedback_template'


class MdlFeedbackValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.BigIntegerField()
    item = models.BigIntegerField()
    completed = models.BigIntegerField()
    tmp_completed = models.BigIntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_feedback_value'
        unique_together = (('completed', 'item', 'course_id'),)


class MdlFeedbackValuetmp(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.BigIntegerField()
    item = models.BigIntegerField()
    completed = models.BigIntegerField()
    tmp_completed = models.BigIntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_feedback_valuetmp'
        unique_together = (('completed', 'item', 'course_id'),)


class MdlFiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    contenthash = models.CharField(max_length=40)
    pathnamehash = models.CharField(unique=True, max_length=40)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    filearea = models.CharField(max_length=50)
    itemid = models.BigIntegerField()
    filepath = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    userid = models.BigIntegerField(blank=True, null=True)
    filesize = models.BigIntegerField()
    mimetype = models.CharField(max_length=100, blank=True, null=True)
    status = models.BigIntegerField()
    source = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    referencefileid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_files'


class MdlFilesReference(models.Model):
    id = models.BigAutoField(primary_key=True)
    repositoryid = models.BigIntegerField()
    lastsync = models.BigIntegerField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    referencehash = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'mdl_files_reference'
        unique_together = (('referencehash', 'repositoryid'),)


class MdlFilterActive(models.Model):
    id = models.BigAutoField(primary_key=True)
    filter = models.CharField(max_length=32)
    contextid = models.BigIntegerField()
    active = models.SmallIntegerField()
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_filter_active'
        unique_together = (('contextid', 'filter'),)


class MdlFilterConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    filter = models.CharField(max_length=32)
    contextid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_filter_config'
        unique_together = (('contextid', 'filter', 'name'),)


class MdlFolder(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    revision = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    display = models.SmallIntegerField()
    showexpanded = models.SmallIntegerField()
    showdownloadfolder = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_folder'


class MdlForum(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    assessed = models.BigIntegerField()
    assesstimestart = models.BigIntegerField()
    assesstimefinish = models.BigIntegerField()
    scale = models.BigIntegerField()
    maxbytes = models.BigIntegerField()
    maxattachments = models.BigIntegerField()
    forcesubscribe = models.SmallIntegerField()
    trackingtype = models.SmallIntegerField()
    rsstype = models.SmallIntegerField()
    rssarticles = models.SmallIntegerField()
    timemodified = models.BigIntegerField()
    warnafter = models.BigIntegerField()
    blockafter = models.BigIntegerField()
    blockperiod = models.BigIntegerField()
    completiondiscussions = models.IntegerField()
    completionreplies = models.IntegerField()
    completionposts = models.IntegerField()
    displaywordcount = models.SmallIntegerField()
    lockdiscussionafter = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_forum'


class MdlForumDigests(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    forum = models.BigIntegerField()
    maildigest = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_forum_digests'
        unique_together = (('forum', 'userid', 'maildigest'),)


class MdlForumDiscussionSubs(models.Model):
    id = models.BigAutoField(primary_key=True)
    forum = models.BigIntegerField()
    userid = models.BigIntegerField()
    discussion = models.BigIntegerField()
    preference = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_forum_discussion_subs'
        unique_together = (('userid', 'discussion'),)


class MdlForumDiscussions(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    forum = models.BigIntegerField()
    name = models.CharField(max_length=255)
    firstpost = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    assessed = models.SmallIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    pinned = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_forum_discussions'


class MdlForumPosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    discussion = models.BigIntegerField()
    parent = models.BigIntegerField()
    userid = models.BigIntegerField()
    created = models.BigIntegerField()
    modified = models.BigIntegerField()
    mailed = models.SmallIntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    messageformat = models.SmallIntegerField()
    messagetrust = models.SmallIntegerField()
    attachment = models.CharField(max_length=100)
    totalscore = models.SmallIntegerField()
    mailnow = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_forum_posts'


class MdlForumQueue(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    discussionid = models.BigIntegerField()
    postid = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_forum_queue'


class MdlForumRead(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    forumid = models.BigIntegerField()
    discussionid = models.BigIntegerField()
    postid = models.BigIntegerField()
    firstread = models.BigIntegerField()
    lastread = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_forum_read'


class MdlForumSubscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    forum = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_forum_subscriptions'


class MdlForumTrackPrefs(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    forumid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_forum_track_prefs'


class MdlGlossary(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    allowduplicatedentries = models.SmallIntegerField()
    displayformat = models.CharField(max_length=50)
    mainglossary = models.SmallIntegerField()
    showspecial = models.SmallIntegerField()
    showalphabet = models.SmallIntegerField()
    showall = models.SmallIntegerField()
    allowcomments = models.SmallIntegerField()
    allowprintview = models.SmallIntegerField()
    usedynalink = models.SmallIntegerField()
    defaultapproval = models.SmallIntegerField()
    approvaldisplayformat = models.CharField(max_length=50)
    globalglossary = models.SmallIntegerField()
    entbypage = models.SmallIntegerField()
    editalways = models.SmallIntegerField()
    rsstype = models.SmallIntegerField()
    rssarticles = models.SmallIntegerField()
    assessed = models.BigIntegerField()
    assesstimestart = models.BigIntegerField()
    assesstimefinish = models.BigIntegerField()
    scale = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionentries = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_glossary'


class MdlGlossaryAlias(models.Model):
    id = models.BigAutoField(primary_key=True)
    entryid = models.BigIntegerField()
    alias = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_glossary_alias'


class MdlGlossaryCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    glossaryid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    usedynalink = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_glossary_categories'


class MdlGlossaryEntries(models.Model):
    id = models.BigAutoField(primary_key=True)
    glossaryid = models.BigIntegerField()
    userid = models.BigIntegerField()
    concept = models.CharField(max_length=255)
    definition = models.TextField()
    definitionformat = models.SmallIntegerField()
    definitiontrust = models.SmallIntegerField()
    attachment = models.CharField(max_length=100)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    teacherentry = models.SmallIntegerField()
    sourceglossaryid = models.BigIntegerField()
    usedynalink = models.SmallIntegerField()
    casesensitive = models.SmallIntegerField()
    fullmatch = models.SmallIntegerField()
    approved = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_glossary_entries'


class MdlGlossaryEntriesCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    categoryid = models.BigIntegerField()
    entryid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_glossary_entries_categories'


class MdlGlossaryFormats(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    popupformatname = models.CharField(max_length=50)
    visible = models.SmallIntegerField()
    showgroup = models.SmallIntegerField()
    showtabs = models.CharField(max_length=100, blank=True, null=True)
    defaultmode = models.CharField(max_length=50)
    defaulthook = models.CharField(max_length=50)
    sortkey = models.CharField(max_length=50)
    sortorder = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mdl_glossary_formats'


class MdlGradeCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    parent = models.BigIntegerField(blank=True, null=True)
    depth = models.BigIntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255)
    aggregation = models.BigIntegerField()
    keephigh = models.BigIntegerField()
    droplow = models.BigIntegerField()
    aggregateonlygraded = models.SmallIntegerField()
    aggregateoutcomes = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    hidden = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_grade_categories'


class MdlGradeCategoriesHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField()
    parent = models.BigIntegerField(blank=True, null=True)
    depth = models.BigIntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255)
    aggregation = models.BigIntegerField()
    keephigh = models.BigIntegerField()
    droplow = models.BigIntegerField()
    aggregateonlygraded = models.SmallIntegerField()
    aggregateoutcomes = models.SmallIntegerField()
    aggregatesubcats = models.SmallIntegerField()
    hidden = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_grade_categories_history'


class MdlGradeGrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemid = models.BigIntegerField()
    userid = models.BigIntegerField()
    rawgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    rawgrademax = models.DecimalField(max_digits=10, decimal_places=5)
    rawgrademin = models.DecimalField(max_digits=10, decimal_places=5)
    rawscaleid = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField(blank=True, null=True)
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    exported = models.BigIntegerField()
    overridden = models.BigIntegerField()
    excluded = models.BigIntegerField()
    feedback = models.TextField(blank=True, null=True)
    feedbackformat = models.BigIntegerField()
    information = models.TextField(blank=True, null=True)
    informationformat = models.BigIntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    aggregationstatus = models.CharField(max_length=10)
    aggregationweight = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_grade_grades'
        unique_together = (('userid', 'itemid'),)


class MdlGradeGradesHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    itemid = models.BigIntegerField()
    userid = models.BigIntegerField()
    rawgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    rawgrademax = models.DecimalField(max_digits=10, decimal_places=5)
    rawgrademin = models.DecimalField(max_digits=10, decimal_places=5)
    rawscaleid = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField(blank=True, null=True)
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    exported = models.BigIntegerField()
    overridden = models.BigIntegerField()
    excluded = models.BigIntegerField()
    feedback = models.TextField(blank=True, null=True)
    feedbackformat = models.BigIntegerField()
    information = models.TextField(blank=True, null=True)
    informationformat = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_grade_grades_history'


class MdlGradeImportNewitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemname = models.CharField(max_length=255)
    importcode = models.BigIntegerField()
    importer = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_grade_import_newitem'


class MdlGradeImportValues(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemid = models.BigIntegerField(blank=True, null=True)
    newgradeitem = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField()
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    importcode = models.BigIntegerField()
    importer = models.BigIntegerField(blank=True, null=True)
    importonlyfeedback = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_grade_import_values'


class MdlGradeItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    categoryid = models.BigIntegerField(blank=True, null=True)
    itemname = models.CharField(max_length=255, blank=True, null=True)
    itemtype = models.CharField(max_length=30)
    itemmodule = models.CharField(max_length=30, blank=True, null=True)
    iteminstance = models.BigIntegerField(blank=True, null=True)
    itemnumber = models.BigIntegerField(blank=True, null=True)
    iteminfo = models.TextField(blank=True, null=True)
    idnumber = models.CharField(max_length=255, blank=True, null=True)
    calculation = models.TextField(blank=True, null=True)
    gradetype = models.SmallIntegerField()
    grademax = models.DecimalField(max_digits=10, decimal_places=5)
    grademin = models.DecimalField(max_digits=10, decimal_places=5)
    scaleid = models.BigIntegerField(blank=True, null=True)
    outcomeid = models.BigIntegerField(blank=True, null=True)
    gradepass = models.DecimalField(max_digits=10, decimal_places=5)
    multfactor = models.DecimalField(max_digits=10, decimal_places=5)
    plusfactor = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef2 = models.DecimalField(max_digits=10, decimal_places=5)
    sortorder = models.BigIntegerField()
    display = models.BigIntegerField()
    decimals = models.SmallIntegerField(blank=True, null=True)
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    needsupdate = models.BigIntegerField()
    weightoverride = models.SmallIntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_grade_items'


class MdlGradeItemsHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    categoryid = models.BigIntegerField(blank=True, null=True)
    itemname = models.CharField(max_length=255, blank=True, null=True)
    itemtype = models.CharField(max_length=30)
    itemmodule = models.CharField(max_length=30, blank=True, null=True)
    iteminstance = models.BigIntegerField(blank=True, null=True)
    itemnumber = models.BigIntegerField(blank=True, null=True)
    iteminfo = models.TextField(blank=True, null=True)
    idnumber = models.CharField(max_length=255, blank=True, null=True)
    calculation = models.TextField(blank=True, null=True)
    gradetype = models.SmallIntegerField()
    grademax = models.DecimalField(max_digits=10, decimal_places=5)
    grademin = models.DecimalField(max_digits=10, decimal_places=5)
    scaleid = models.BigIntegerField(blank=True, null=True)
    outcomeid = models.BigIntegerField(blank=True, null=True)
    gradepass = models.DecimalField(max_digits=10, decimal_places=5)
    multfactor = models.DecimalField(max_digits=10, decimal_places=5)
    plusfactor = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef2 = models.DecimalField(max_digits=10, decimal_places=5)
    sortorder = models.BigIntegerField()
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    needsupdate = models.BigIntegerField()
    display = models.BigIntegerField()
    decimals = models.SmallIntegerField(blank=True, null=True)
    weightoverride = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_grade_items_history'


class MdlGradeLetters(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    lowerboundary = models.DecimalField(max_digits=10, decimal_places=5)
    letter = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_grade_letters'
        unique_together = (('contextid', 'lowerboundary', 'letter'),)


class MdlGradeOutcomes(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=255)
    fullname = models.TextField()
    scaleid = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_grade_outcomes'
        unique_together = (('courseid', 'shortname'),)


class MdlGradeOutcomesCourses(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    outcomeid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_grade_outcomes_courses'
        unique_together = (('courseid', 'outcomeid'),)


class MdlGradeOutcomesHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=255)
    fullname = models.TextField()
    scaleid = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_grade_outcomes_history'


class MdlGradeSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_grade_settings'
        unique_together = (('courseid', 'name'),)


class MdlGradingAreas(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    areaname = models.CharField(max_length=100)
    activemethod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_grading_areas'
        unique_together = (('contextid', 'component', 'areaname'),)


class MdlGradingDefinitions(models.Model):
    id = models.BigAutoField(primary_key=True)
    areaid = models.BigIntegerField()
    method = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)
    status = models.BigIntegerField()
    copiedfromid = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    usercreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    timecopied = models.BigIntegerField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_grading_definitions'
        unique_together = (('areaid', 'method'),)


class MdlGradingInstances(models.Model):
    id = models.BigAutoField(primary_key=True)
    definitionid = models.BigIntegerField()
    raterid = models.BigIntegerField()
    itemid = models.BigIntegerField(blank=True, null=True)
    rawgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    status = models.BigIntegerField()
    feedback = models.TextField(blank=True, null=True)
    feedbackformat = models.SmallIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_grading_instances'


class MdlGradingformGuideComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    definitionid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_gradingform_guide_comments'


class MdlGradingformGuideCriteria(models.Model):
    id = models.BigAutoField(primary_key=True)
    definitionid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    shortname = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)
    descriptionmarkers = models.TextField(blank=True, null=True)
    descriptionmarkersformat = models.SmallIntegerField(blank=True, null=True)
    maxscore = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'mdl_gradingform_guide_criteria'


class MdlGradingformGuideFillings(models.Model):
    id = models.BigAutoField(primary_key=True)
    instanceid = models.BigIntegerField()
    criterionid = models.BigIntegerField()
    remark = models.TextField(blank=True, null=True)
    remarkformat = models.SmallIntegerField(blank=True, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'mdl_gradingform_guide_fillings'
        unique_together = (('instanceid', 'criterionid'),)


class MdlGradingformRubricCriteria(models.Model):
    id = models.BigAutoField(primary_key=True)
    definitionid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_gradingform_rubric_criteria'


class MdlGradingformRubricFillings(models.Model):
    id = models.BigAutoField(primary_key=True)
    instanceid = models.BigIntegerField()
    criterionid = models.BigIntegerField()
    levelid = models.BigIntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    remarkformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_gradingform_rubric_fillings'
        unique_together = (('instanceid', 'criterionid'),)


class MdlGradingformRubricLevels(models.Model):
    id = models.BigAutoField(primary_key=True)
    criterionid = models.BigIntegerField()
    score = models.DecimalField(max_digits=10, decimal_places=5)
    definition = models.TextField(blank=True, null=True)
    definitionformat = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_gradingform_rubric_levels'


class MdlGroupings(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    configdata = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_groupings'


class MdlGroupingsGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    groupingid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    timeadded = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_groupings_groups'


class MdlGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    idnumber = models.CharField(max_length=100)
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    enrolmentkey = models.CharField(max_length=50, blank=True, null=True)
    picture = models.BigIntegerField()
    hidepicture = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_groups'


class MdlGroupsMembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timeadded = models.BigIntegerField()
    component = models.CharField(max_length=100)
    itemid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_groups_members'


class MdlImscp(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    revision = models.BigIntegerField()
    keepold = models.BigIntegerField()
    structure = models.TextField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_imscp'


class MdlLabel(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_label'


class MdlLesson(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    practice = models.SmallIntegerField()
    modattempts = models.SmallIntegerField()
    usepassword = models.SmallIntegerField()
    password = models.CharField(max_length=32)
    dependency = models.BigIntegerField()
    conditions = models.TextField()
    grade = models.BigIntegerField()
    custom = models.SmallIntegerField()
    ongoing = models.SmallIntegerField()
    usemaxgrade = models.SmallIntegerField()
    maxanswers = models.SmallIntegerField()
    maxattempts = models.SmallIntegerField()
    review = models.SmallIntegerField()
    nextpagedefault = models.SmallIntegerField()
    feedback = models.SmallIntegerField()
    minquestions = models.SmallIntegerField()
    maxpages = models.SmallIntegerField()
    timelimit = models.BigIntegerField()
    retake = models.SmallIntegerField()
    activitylink = models.BigIntegerField()
    mediafile = models.CharField(max_length=255)
    mediaheight = models.BigIntegerField()
    mediawidth = models.BigIntegerField()
    mediaclose = models.SmallIntegerField()
    slideshow = models.SmallIntegerField()
    width = models.BigIntegerField()
    height = models.BigIntegerField()
    bgcolor = models.CharField(max_length=7)
    displayleft = models.SmallIntegerField()
    displayleftif = models.SmallIntegerField()
    progressbar = models.SmallIntegerField()
    available = models.BigIntegerField()
    deadline = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionendreached = models.SmallIntegerField(blank=True, null=True)
    completiontimespent = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_lesson'


class MdlLessonAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    jumpto = models.BigIntegerField()
    grade = models.SmallIntegerField()
    score = models.BigIntegerField()
    flags = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    answer = models.TextField(blank=True, null=True)
    answerformat = models.SmallIntegerField()
    response = models.TextField(blank=True, null=True)
    responseformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_lesson_answers'


class MdlLessonAttempts(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    userid = models.BigIntegerField()
    answerid = models.BigIntegerField()
    retry = models.SmallIntegerField()
    correct = models.BigIntegerField()
    useranswer = models.TextField(blank=True, null=True)
    timeseen = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_lesson_attempts'


class MdlLessonBranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    userid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    retry = models.BigIntegerField()
    flag = models.SmallIntegerField()
    timeseen = models.BigIntegerField()
    nextpageid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_lesson_branch'


class MdlLessonGrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    userid = models.BigIntegerField()
    grade = models.FloatField()
    late = models.SmallIntegerField()
    completed = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_lesson_grades'


class MdlLessonOverrides(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    groupid = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    available = models.BigIntegerField(blank=True, null=True)
    deadline = models.BigIntegerField(blank=True, null=True)
    timelimit = models.BigIntegerField(blank=True, null=True)
    review = models.SmallIntegerField(blank=True, null=True)
    maxattempts = models.SmallIntegerField(blank=True, null=True)
    retake = models.SmallIntegerField(blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_lesson_overrides'


class MdlLessonPages(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    prevpageid = models.BigIntegerField()
    nextpageid = models.BigIntegerField()
    qtype = models.SmallIntegerField()
    qoption = models.SmallIntegerField()
    layout = models.SmallIntegerField()
    display = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    title = models.CharField(max_length=255)
    contents = models.TextField()
    contentsformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_lesson_pages'


class MdlLessonTimer(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    userid = models.BigIntegerField()
    starttime = models.BigIntegerField()
    lessontime = models.BigIntegerField()
    completed = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_lesson_timer'


class MdlLicense(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.SmallIntegerField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_license'


class MdlLockDb(models.Model):
    id = models.BigAutoField(primary_key=True)
    resourcekey = models.CharField(unique=True, max_length=255)
    expires = models.BigIntegerField(blank=True, null=True)
    owner = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_lock_db'


class MdlLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.BigIntegerField()
    userid = models.BigIntegerField()
    ip = models.CharField(max_length=45)
    course = models.BigIntegerField()
    module = models.CharField(max_length=20)
    cmid = models.BigIntegerField()
    action = models.CharField(max_length=40)
    url = models.CharField(max_length=100)
    info = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_log'


class MdlLogDisplay(models.Model):
    id = models.BigAutoField(primary_key=True)
    module = models.CharField(max_length=20)
    action = models.CharField(max_length=40)
    mtable = models.CharField(max_length=30)
    field = models.CharField(max_length=200)
    component = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'mdl_log_display'
        unique_together = (('module', 'action'),)


class MdlLogQueries(models.Model):
    id = models.BigAutoField(primary_key=True)
    qtype = models.IntegerField()
    sqltext = models.TextField()
    sqlparams = models.TextField(blank=True, null=True)
    error = models.IntegerField()
    info = models.TextField(blank=True, null=True)
    backtrace = models.TextField(blank=True, null=True)
    exectime = models.DecimalField(max_digits=10, decimal_places=5)
    timelogged = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_log_queries'


class MdlLogstoreStandardLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    eventname = models.CharField(max_length=255)
    component = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    objecttable = models.CharField(max_length=50, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    crud = models.CharField(max_length=1)
    edulevel = models.SmallIntegerField()
    contextid = models.BigIntegerField()
    contextlevel = models.BigIntegerField()
    contextinstanceid = models.BigIntegerField()
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField(blank=True, null=True)
    relateduserid = models.BigIntegerField(blank=True, null=True)
    anonymous = models.SmallIntegerField()
    other = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    origin = models.CharField(max_length=10, blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)
    realuserid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_logstore_standard_log'


class MdlLti(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    typeid = models.BigIntegerField(blank=True, null=True)
    toolurl = models.TextField()
    securetoolurl = models.TextField(blank=True, null=True)
    instructorchoicesendname = models.SmallIntegerField(blank=True, null=True)
    instructorchoicesendemailaddr = models.SmallIntegerField(blank=True, null=True)
    instructorchoiceallowroster = models.SmallIntegerField(blank=True, null=True)
    instructorchoiceallowsetting = models.SmallIntegerField(blank=True, null=True)
    instructorcustomparameters = models.CharField(max_length=255, blank=True, null=True)
    instructorchoiceacceptgrades = models.SmallIntegerField(blank=True, null=True)
    grade = models.BigIntegerField()
    launchcontainer = models.SmallIntegerField()
    resourcekey = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    debuglaunch = models.SmallIntegerField()
    showtitlelaunch = models.SmallIntegerField()
    showdescriptionlaunch = models.SmallIntegerField()
    servicesalt = models.CharField(max_length=40, blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    secureicon = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_lti'


class MdlLtiSubmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    ltiid = models.BigIntegerField()
    userid = models.BigIntegerField()
    datesubmitted = models.BigIntegerField()
    dateupdated = models.BigIntegerField()
    gradepercent = models.DecimalField(max_digits=10, decimal_places=5)
    originalgrade = models.DecimalField(max_digits=10, decimal_places=5)
    launchid = models.BigIntegerField()
    state = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_lti_submission'


class MdlLtiToolProxies(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    regurl = models.TextField(blank=True, null=True)
    state = models.SmallIntegerField()
    guid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    secret = models.CharField(max_length=255, blank=True, null=True)
    vendorcode = models.CharField(max_length=255, blank=True, null=True)
    capabilityoffered = models.TextField()
    serviceoffered = models.TextField()
    toolproxy = models.TextField(blank=True, null=True)
    createdby = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_lti_tool_proxies'


class MdlLtiToolSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    toolproxyid = models.BigIntegerField()
    course = models.BigIntegerField(blank=True, null=True)
    coursemoduleid = models.BigIntegerField(blank=True, null=True)
    settings = models.TextField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_lti_tool_settings'


class MdlLtiTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    baseurl = models.TextField()
    tooldomain = models.CharField(max_length=255)
    state = models.SmallIntegerField()
    course = models.BigIntegerField()
    coursevisible = models.SmallIntegerField()
    toolproxyid = models.BigIntegerField(blank=True, null=True)
    enabledcapability = models.TextField(blank=True, null=True)
    parameter = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    secureicon = models.TextField(blank=True, null=True)
    createdby = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_lti_types'


class MdlLtiTypesConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    typeid = models.BigIntegerField()
    name = models.CharField(max_length=100)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_lti_types_config'


class MdlMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    useridfrom = models.BigIntegerField()
    useridto = models.BigIntegerField()
    subject = models.TextField(blank=True, null=True)
    fullmessage = models.TextField(blank=True, null=True)
    fullmessageformat = models.SmallIntegerField(blank=True, null=True)
    fullmessagehtml = models.TextField(blank=True, null=True)
    smallmessage = models.TextField(blank=True, null=True)
    notification = models.SmallIntegerField(blank=True, null=True)
    contexturl = models.TextField(blank=True, null=True)
    contexturlname = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timeuserfromdeleted = models.BigIntegerField()
    timeusertodeleted = models.BigIntegerField()
    component = models.CharField(max_length=100, blank=True, null=True)
    eventtype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_message'


class MdlMessageAirnotifierDevices(models.Model):
    id = models.BigAutoField(primary_key=True)
    userdeviceid = models.BigIntegerField(unique=True)
    enable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_message_airnotifier_devices'


class MdlMessageContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    contactid = models.BigIntegerField()
    blocked = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_message_contacts'
        unique_together = (('userid', 'contactid'),)


class MdlMessagePopup(models.Model):
    id = models.BigAutoField(primary_key=True)
    messageid = models.BigIntegerField()
    isread = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_message_popup'
        unique_together = (('messageid', 'isread'),)


class MdlMessageProcessors(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=166)
    enabled = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_message_processors'


class MdlMessageProviders(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    component = models.CharField(max_length=200)
    capability = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_message_providers'
        unique_together = (('component', 'name'),)


class MdlMessageRead(models.Model):
    id = models.BigAutoField(primary_key=True)
    useridfrom = models.BigIntegerField()
    useridto = models.BigIntegerField()
    subject = models.TextField(blank=True, null=True)
    fullmessage = models.TextField(blank=True, null=True)
    fullmessageformat = models.SmallIntegerField(blank=True, null=True)
    fullmessagehtml = models.TextField(blank=True, null=True)
    smallmessage = models.TextField(blank=True, null=True)
    notification = models.SmallIntegerField(blank=True, null=True)
    contexturl = models.TextField(blank=True, null=True)
    contexturlname = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timeread = models.BigIntegerField()
    timeuserfromdeleted = models.BigIntegerField()
    timeusertodeleted = models.BigIntegerField()
    component = models.CharField(max_length=100, blank=True, null=True)
    eventtype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_message_read'


class MdlMessageWorking(models.Model):
    id = models.BigAutoField(primary_key=True)
    unreadmessageid = models.BigIntegerField()
    processorid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_message_working'


class MdlMessageinboundDatakeys(models.Model):
    id = models.BigAutoField(primary_key=True)
    handler = models.BigIntegerField()
    datavalue = models.BigIntegerField()
    datakey = models.CharField(max_length=64, blank=True, null=True)
    timecreated = models.BigIntegerField()
    expires = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_messageinbound_datakeys'
        unique_together = (('handler', 'datavalue'),)


class MdlMessageinboundHandlers(models.Model):
    id = models.BigAutoField(primary_key=True)
    component = models.CharField(max_length=100)
    classname = models.CharField(unique=True, max_length=255)
    defaultexpiration = models.BigIntegerField()
    validateaddress = models.SmallIntegerField()
    enabled = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_messageinbound_handlers'


class MdlMessageinboundMessagelist(models.Model):
    id = models.BigAutoField(primary_key=True)
    messageid = models.TextField()
    userid = models.BigIntegerField()
    address = models.TextField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_messageinbound_messagelist'


class MdlMnetApplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    xmlrpc_server_url = models.CharField(max_length=255)
    sso_land_url = models.CharField(max_length=255)
    sso_jump_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_mnet_application'


class MdlMnetHost(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted = models.SmallIntegerField()
    wwwroot = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=45)
    name = models.CharField(max_length=80)
    public_key = models.TextField()
    public_key_expires = models.BigIntegerField()
    transport = models.SmallIntegerField()
    portno = models.IntegerField()
    last_connect_time = models.BigIntegerField()
    last_log_id = models.BigIntegerField()
    force_theme = models.SmallIntegerField()
    theme = models.CharField(max_length=100, blank=True, null=True)
    applicationid = models.BigIntegerField()
    sslverification = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_mnet_host'


class MdlMnetHost2Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    hostid = models.BigIntegerField()
    serviceid = models.BigIntegerField()
    publish = models.SmallIntegerField()
    subscribe = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_mnet_host2service'
        unique_together = (('hostid', 'serviceid'),)


class MdlMnetLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    hostid = models.BigIntegerField()
    remoteid = models.BigIntegerField()
    time = models.BigIntegerField()
    userid = models.BigIntegerField()
    ip = models.CharField(max_length=45)
    course = models.BigIntegerField()
    coursename = models.CharField(max_length=40)
    module = models.CharField(max_length=20)
    cmid = models.BigIntegerField()
    action = models.CharField(max_length=40)
    url = models.CharField(max_length=100)
    info = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_mnet_log'


class MdlMnetRemoteRpc(models.Model):
    id = models.BigAutoField(primary_key=True)
    functionname = models.CharField(max_length=40)
    xmlrpcpath = models.CharField(max_length=80)
    plugintype = models.CharField(max_length=20)
    pluginname = models.CharField(max_length=20)
    enabled = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_mnet_remote_rpc'


class MdlMnetRemoteService2Rpc(models.Model):
    id = models.BigAutoField(primary_key=True)
    serviceid = models.BigIntegerField()
    rpcid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_mnet_remote_service2rpc'
        unique_together = (('rpcid', 'serviceid'),)


class MdlMnetRpc(models.Model):
    id = models.BigAutoField(primary_key=True)
    functionname = models.CharField(max_length=40)
    xmlrpcpath = models.CharField(max_length=80)
    plugintype = models.CharField(max_length=20)
    pluginname = models.CharField(max_length=20)
    enabled = models.SmallIntegerField()
    help = models.TextField()
    profile = models.TextField()
    filename = models.CharField(max_length=100)
    classname = models.CharField(max_length=150, blank=True, null=True)
    static = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_mnet_rpc'


class MdlMnetService(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    apiversion = models.CharField(max_length=10)
    offer = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_mnet_service'


class MdlMnetService2Rpc(models.Model):
    id = models.BigAutoField(primary_key=True)
    serviceid = models.BigIntegerField()
    rpcid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_mnet_service2rpc'
        unique_together = (('rpcid', 'serviceid'),)


class MdlMnetSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    username = models.CharField(max_length=100)
    token = models.CharField(unique=True, max_length=40)
    mnethostid = models.BigIntegerField()
    useragent = models.CharField(max_length=40)
    confirm_timeout = models.BigIntegerField()
    session_id = models.CharField(max_length=40)
    expires = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_mnet_session'


class MdlMnetSsoAccessControl(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)
    mnet_host_id = models.BigIntegerField()
    accessctrl = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mdl_mnet_sso_access_control'
        unique_together = (('mnet_host_id', 'username'),)


class MdlMnetserviceEnrolCourses(models.Model):
    id = models.BigAutoField(primary_key=True)
    hostid = models.BigIntegerField()
    remoteid = models.BigIntegerField()
    categoryid = models.BigIntegerField()
    categoryname = models.CharField(max_length=255)
    sortorder = models.BigIntegerField()
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=100)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField()
    summaryformat = models.SmallIntegerField(blank=True, null=True)
    startdate = models.BigIntegerField()
    roleid = models.BigIntegerField()
    rolename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_mnetservice_enrol_courses'
        unique_together = (('hostid', 'remoteid'),)


class MdlMnetserviceEnrolEnrolments(models.Model):
    id = models.BigAutoField(primary_key=True)
    hostid = models.BigIntegerField()
    userid = models.BigIntegerField()
    remotecourseid = models.BigIntegerField()
    rolename = models.CharField(max_length=255)
    enroltime = models.BigIntegerField()
    enroltype = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mdl_mnetservice_enrol_enrolments'


class MdlModules(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    cron = models.BigIntegerField()
    lastcron = models.BigIntegerField()
    search = models.CharField(max_length=255)
    visible = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_modules'


class MdlMyPages(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    private = models.SmallIntegerField()
    sortorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_my_pages'


class MdlPage(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    content = models.TextField(blank=True, null=True)
    contentformat = models.SmallIntegerField()
    legacyfiles = models.SmallIntegerField()
    legacyfileslast = models.BigIntegerField(blank=True, null=True)
    display = models.SmallIntegerField()
    displayoptions = models.TextField(blank=True, null=True)
    revision = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_page'


class MdlPortfolioInstance(models.Model):
    id = models.BigAutoField(primary_key=True)
    plugin = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    visible = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_portfolio_instance'


class MdlPortfolioInstanceConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_portfolio_instance_config'


class MdlPortfolioInstanceUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance = models.BigIntegerField()
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_portfolio_instance_user'


class MdlPortfolioLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    time = models.BigIntegerField()
    portfolio = models.BigIntegerField()
    caller_class = models.CharField(max_length=150)
    caller_file = models.CharField(max_length=255)
    caller_component = models.CharField(max_length=255, blank=True, null=True)
    caller_sha1 = models.CharField(max_length=255)
    tempdataid = models.BigIntegerField()
    returnurl = models.CharField(max_length=255)
    continueurl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_portfolio_log'


class MdlPortfolioMaharaQueue(models.Model):
    id = models.BigAutoField(primary_key=True)
    transferid = models.BigIntegerField()
    token = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mdl_portfolio_mahara_queue'


class MdlPortfolioTempdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    expirytime = models.BigIntegerField()
    userid = models.BigIntegerField()
    instance = models.BigIntegerField(blank=True, null=True)
    queued = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_portfolio_tempdata'


class MdlPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    module = models.CharField(max_length=20)
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    moduleid = models.BigIntegerField()
    coursemoduleid = models.BigIntegerField()
    subject = models.CharField(max_length=128)
    summary = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    uniquehash = models.CharField(max_length=255)
    rating = models.BigIntegerField()
    format = models.BigIntegerField()
    summaryformat = models.SmallIntegerField()
    attachment = models.CharField(max_length=100, blank=True, null=True)
    publishstate = models.CharField(max_length=20)
    lastmodified = models.BigIntegerField()
    created = models.BigIntegerField()
    usermodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_post'
        unique_together = (('id', 'userid'),)


class MdlProfiling(models.Model):
    id = models.BigAutoField(primary_key=True)
    runid = models.CharField(unique=True, max_length=32)
    url = models.CharField(max_length=255)
    data = models.TextField()
    totalexecutiontime = models.BigIntegerField()
    totalcputime = models.BigIntegerField()
    totalcalls = models.BigIntegerField()
    totalmemory = models.BigIntegerField()
    runreference = models.SmallIntegerField()
    runcomment = models.CharField(max_length=255)
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_profiling'


class MdlQtypeDdimageortext(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    shuffleanswers = models.SmallIntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.SmallIntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.SmallIntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.SmallIntegerField()
    shownumcorrect = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_qtype_ddimageortext'


class MdlQtypeDdimageortextDrags(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    no = models.BigIntegerField()
    draggroup = models.BigIntegerField()
    infinite = models.SmallIntegerField()
    label = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_qtype_ddimageortext_drags'


class MdlQtypeDdimageortextDrops(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    no = models.BigIntegerField()
    xleft = models.BigIntegerField()
    ytop = models.BigIntegerField()
    choice = models.BigIntegerField()
    label = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_qtype_ddimageortext_drops'


class MdlQtypeDdmarker(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    shuffleanswers = models.SmallIntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.SmallIntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.SmallIntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.SmallIntegerField()
    shownumcorrect = models.SmallIntegerField()
    showmisplaced = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_qtype_ddmarker'


class MdlQtypeDdmarkerDrags(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    no = models.BigIntegerField()
    label = models.TextField()
    infinite = models.SmallIntegerField()
    noofdrags = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_qtype_ddmarker_drags'


class MdlQtypeDdmarkerDrops(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    no = models.BigIntegerField()
    shape = models.CharField(max_length=255, blank=True, null=True)
    coords = models.TextField()
    choice = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_qtype_ddmarker_drops'


class MdlQtypeEssayOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    responseformat = models.CharField(max_length=16)
    responserequired = models.SmallIntegerField()
    responsefieldlines = models.SmallIntegerField()
    attachments = models.SmallIntegerField()
    attachmentsrequired = models.SmallIntegerField()
    graderinfo = models.TextField(blank=True, null=True)
    graderinfoformat = models.SmallIntegerField()
    responsetemplate = models.TextField(blank=True, null=True)
    responsetemplateformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_qtype_essay_options'


class MdlQtypeMatchOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    shuffleanswers = models.SmallIntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.SmallIntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.SmallIntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.SmallIntegerField()
    shownumcorrect = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_qtype_match_options'


class MdlQtypeMatchSubquestions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    questiontext = models.TextField()
    questiontextformat = models.SmallIntegerField()
    answertext = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_qtype_match_subquestions'


class MdlQtypeMultichoiceOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    layout = models.SmallIntegerField()
    single = models.SmallIntegerField()
    shuffleanswers = models.SmallIntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.SmallIntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.SmallIntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.SmallIntegerField()
    answernumbering = models.CharField(max_length=10)
    shownumcorrect = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_qtype_multichoice_options'


class MdlQtypeRandomsamatchOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    choose = models.BigIntegerField()
    subcats = models.SmallIntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.SmallIntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.SmallIntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.SmallIntegerField()
    shownumcorrect = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_qtype_randomsamatch_options'


class MdlQtypeShortanswerOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    usecase = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_qtype_shortanswer_options'


class MdlQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.BigIntegerField()
    parent = models.BigIntegerField()
    name = models.CharField(max_length=255)
    questiontext = models.TextField()
    questiontextformat = models.SmallIntegerField()
    generalfeedback = models.TextField()
    generalfeedbackformat = models.SmallIntegerField()
    defaultmark = models.DecimalField(max_digits=12, decimal_places=7)
    penalty = models.DecimalField(max_digits=12, decimal_places=7)
    qtype = models.CharField(max_length=20)
    length = models.BigIntegerField()
    stamp = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    hidden = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_question'


class MdlQuestionAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    answer = models.TextField()
    answerformat = models.SmallIntegerField()
    fraction = models.DecimalField(max_digits=12, decimal_places=7)
    feedback = models.TextField()
    feedbackformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_question_answers'


class MdlQuestionAttemptStepData(models.Model):
    id = models.BigAutoField(primary_key=True)
    attemptstepid = models.BigIntegerField()
    name = models.CharField(max_length=32)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_question_attempt_step_data'


class MdlQuestionAttemptSteps(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionattemptid = models.BigIntegerField()
    sequencenumber = models.BigIntegerField()
    state = models.CharField(max_length=13)
    fraction = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    timecreated = models.BigIntegerField()
    userid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_question_attempt_steps'
        unique_together = (('questionattemptid', 'sequencenumber'),)


class MdlQuestionAttempts(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionusageid = models.BigIntegerField()
    slot = models.BigIntegerField()
    behaviour = models.CharField(max_length=32)
    questionid = models.BigIntegerField()
    variant = models.BigIntegerField()
    maxmark = models.DecimalField(max_digits=12, decimal_places=7)
    minfraction = models.DecimalField(max_digits=12, decimal_places=7)
    maxfraction = models.DecimalField(max_digits=12, decimal_places=7)
    flagged = models.SmallIntegerField()
    questionsummary = models.TextField(blank=True, null=True)
    rightanswer = models.TextField(blank=True, null=True)
    responsesummary = models.TextField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_question_attempts'
        unique_together = (('questionusageid', 'slot'),)


class MdlQuestionCalculated(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    answer = models.BigIntegerField()
    tolerance = models.CharField(max_length=20)
    tolerancetype = models.BigIntegerField()
    correctanswerlength = models.BigIntegerField()
    correctanswerformat = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_question_calculated'


class MdlQuestionCalculatedOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    synchronize = models.SmallIntegerField()
    single = models.SmallIntegerField()
    shuffleanswers = models.SmallIntegerField()
    correctfeedback = models.TextField(blank=True, null=True)
    correctfeedbackformat = models.SmallIntegerField()
    partiallycorrectfeedback = models.TextField(blank=True, null=True)
    partiallycorrectfeedbackformat = models.SmallIntegerField()
    incorrectfeedback = models.TextField(blank=True, null=True)
    incorrectfeedbackformat = models.SmallIntegerField()
    answernumbering = models.CharField(max_length=10)
    shownumcorrect = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_question_calculated_options'


class MdlQuestionCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contextid = models.BigIntegerField()
    info = models.TextField()
    infoformat = models.SmallIntegerField()
    stamp = models.CharField(max_length=255)
    parent = models.BigIntegerField()
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_question_categories'
        unique_together = (('contextid', 'stamp'),)


class MdlQuestionDatasetDefinitions(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.BigIntegerField()
    name = models.CharField(max_length=255)
    type = models.BigIntegerField()
    options = models.CharField(max_length=255)
    itemcount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_question_dataset_definitions'


class MdlQuestionDatasetItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    definition = models.BigIntegerField()
    itemnumber = models.BigIntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_question_dataset_items'


class MdlQuestionDatasets(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    datasetdefinition = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_question_datasets'


class MdlQuestionDdwtos(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    shuffleanswers = models.SmallIntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.SmallIntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.SmallIntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.SmallIntegerField()
    shownumcorrect = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_question_ddwtos'


class MdlQuestionGapselect(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    shuffleanswers = models.SmallIntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.SmallIntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.SmallIntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.SmallIntegerField()
    shownumcorrect = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_question_gapselect'


class MdlQuestionHints(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    hint = models.TextField()
    hintformat = models.SmallIntegerField()
    shownumcorrect = models.SmallIntegerField(blank=True, null=True)
    clearwrong = models.SmallIntegerField(blank=True, null=True)
    options = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_question_hints'


class MdlQuestionMultianswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    sequence = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_question_multianswer'


class MdlQuestionNumerical(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    answer = models.BigIntegerField()
    tolerance = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_question_numerical'


class MdlQuestionNumericalOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    showunits = models.SmallIntegerField()
    unitsleft = models.SmallIntegerField()
    unitgradingtype = models.SmallIntegerField()
    unitpenalty = models.DecimalField(max_digits=12, decimal_places=7)

    class Meta:
        managed = False
        db_table = 'mdl_question_numerical_options'


class MdlQuestionNumericalUnits(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    multiplier = models.DecimalField(max_digits=40, decimal_places=20)
    unit = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mdl_question_numerical_units'
        unique_together = (('question', 'unit'),)


class MdlQuestionResponseAnalysis(models.Model):
    id = models.BigAutoField(primary_key=True)
    hashcode = models.CharField(max_length=40)
    whichtries = models.CharField(max_length=255)
    timemodified = models.BigIntegerField()
    questionid = models.BigIntegerField()
    variant = models.BigIntegerField(blank=True, null=True)
    subqid = models.CharField(max_length=100)
    aid = models.CharField(max_length=100, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    credit = models.DecimalField(max_digits=15, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'mdl_question_response_analysis'


class MdlQuestionResponseCount(models.Model):
    id = models.BigAutoField(primary_key=True)
    analysisid = models.BigIntegerField()
    try_field = models.BigIntegerField(db_column='try')  # Field renamed because it was a Python reserved word.
    rcount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_question_response_count'


class MdlQuestionStatistics(models.Model):
    id = models.BigAutoField(primary_key=True)
    hashcode = models.CharField(max_length=40)
    timemodified = models.BigIntegerField()
    questionid = models.BigIntegerField()
    slot = models.BigIntegerField(blank=True, null=True)
    subquestion = models.SmallIntegerField()
    variant = models.BigIntegerField(blank=True, null=True)
    s = models.BigIntegerField()
    effectiveweight = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    negcovar = models.SmallIntegerField()
    discriminationindex = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    discriminativeefficiency = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    sd = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    facility = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    subquestions = models.TextField(blank=True, null=True)
    maxmark = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    positions = models.TextField(blank=True, null=True)
    randomguessscore = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_question_statistics'


class MdlQuestionTruefalse(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    trueanswer = models.BigIntegerField()
    falseanswer = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_question_truefalse'


class MdlQuestionUsages(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=255)
    preferredbehaviour = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'mdl_question_usages'


class MdlQuiz(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    timelimit = models.BigIntegerField()
    overduehandling = models.CharField(max_length=16)
    graceperiod = models.BigIntegerField()
    preferredbehaviour = models.CharField(max_length=32)
    canredoquestions = models.SmallIntegerField()
    attempts = models.IntegerField()
    attemptonlast = models.SmallIntegerField()
    grademethod = models.SmallIntegerField()
    decimalpoints = models.SmallIntegerField()
    questiondecimalpoints = models.SmallIntegerField()
    reviewattempt = models.IntegerField()
    reviewcorrectness = models.IntegerField()
    reviewmarks = models.IntegerField()
    reviewspecificfeedback = models.IntegerField()
    reviewgeneralfeedback = models.IntegerField()
    reviewrightanswer = models.IntegerField()
    reviewoverallfeedback = models.IntegerField()
    questionsperpage = models.BigIntegerField()
    navmethod = models.CharField(max_length=16)
    shuffleanswers = models.SmallIntegerField()
    sumgrades = models.DecimalField(max_digits=10, decimal_places=5)
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    password = models.CharField(max_length=255)
    subnet = models.CharField(max_length=255)
    browsersecurity = models.CharField(max_length=32)
    delay1 = models.BigIntegerField()
    delay2 = models.BigIntegerField()
    showuserpicture = models.SmallIntegerField()
    showblocks = models.SmallIntegerField()
    completionattemptsexhausted = models.SmallIntegerField(blank=True, null=True)
    completionpass = models.SmallIntegerField(blank=True, null=True)
    allowofflineattempts = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_quiz'


class MdlQuizAttempts(models.Model):
    id = models.BigAutoField(primary_key=True)
    quiz = models.BigIntegerField()
    userid = models.BigIntegerField()
    attempt = models.IntegerField()
    uniqueid = models.BigIntegerField(unique=True)
    layout = models.TextField()
    currentpage = models.BigIntegerField()
    preview = models.SmallIntegerField()
    state = models.CharField(max_length=16)
    timestart = models.BigIntegerField()
    timefinish = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    timemodifiedoffline = models.BigIntegerField()
    timecheckstate = models.BigIntegerField(blank=True, null=True)
    sumgrades = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_quiz_attempts'
        unique_together = (('quiz', 'userid', 'attempt'),)


class MdlQuizFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    quizid = models.BigIntegerField()
    feedbacktext = models.TextField()
    feedbacktextformat = models.SmallIntegerField()
    mingrade = models.DecimalField(max_digits=10, decimal_places=5)
    maxgrade = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'mdl_quiz_feedback'


class MdlQuizGrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    quiz = models.BigIntegerField()
    userid = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_quiz_grades'


class MdlQuizOverrides(models.Model):
    id = models.BigAutoField(primary_key=True)
    quiz = models.BigIntegerField()
    groupid = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    timeopen = models.BigIntegerField(blank=True, null=True)
    timeclose = models.BigIntegerField(blank=True, null=True)
    timelimit = models.BigIntegerField(blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_quiz_overrides'


class MdlQuizOverviewRegrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionusageid = models.BigIntegerField()
    slot = models.BigIntegerField()
    newfraction = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    oldfraction = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    regraded = models.SmallIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_quiz_overview_regrades'


class MdlQuizReports(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    displayorder = models.BigIntegerField()
    capability = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_quiz_reports'


class MdlQuizSections(models.Model):
    id = models.BigAutoField(primary_key=True)
    quizid = models.BigIntegerField()
    firstslot = models.BigIntegerField()
    heading = models.CharField(max_length=1333, blank=True, null=True)
    shufflequestions = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_quiz_sections'
        unique_together = (('quizid', 'firstslot'),)


class MdlQuizSlots(models.Model):
    id = models.BigAutoField(primary_key=True)
    slot = models.BigIntegerField()
    quizid = models.BigIntegerField()
    page = models.BigIntegerField()
    requireprevious = models.SmallIntegerField()
    questionid = models.BigIntegerField()
    maxmark = models.DecimalField(max_digits=12, decimal_places=7)

    class Meta:
        managed = False
        db_table = 'mdl_quiz_slots'
        unique_together = (('quizid', 'slot'),)


class MdlQuizStatistics(models.Model):
    id = models.BigAutoField(primary_key=True)
    hashcode = models.CharField(max_length=40)
    whichattempts = models.SmallIntegerField()
    timemodified = models.BigIntegerField()
    firstattemptscount = models.BigIntegerField()
    highestattemptscount = models.BigIntegerField()
    lastattemptscount = models.BigIntegerField()
    allattemptscount = models.BigIntegerField()
    firstattemptsavg = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    highestattemptsavg = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    lastattemptsavg = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    allattemptsavg = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    median = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    standarddeviation = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    skewness = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    kurtosis = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    cic = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    errorratio = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    standarderror = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_quiz_statistics'


class MdlRating(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    ratingarea = models.CharField(max_length=50)
    itemid = models.BigIntegerField()
    scaleid = models.BigIntegerField()
    rating = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_rating'


class MdlRegistrationHubs(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=255)
    hubname = models.CharField(max_length=255)
    huburl = models.CharField(max_length=255)
    confirmed = models.SmallIntegerField()
    secret = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_registration_hubs'


class MdlRepository(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=255)
    visible = models.SmallIntegerField(blank=True, null=True)
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_repository'


class MdlRepositoryInstanceConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    instanceid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_repository_instance_config'


class MdlRepositoryInstances(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    typeid = models.BigIntegerField()
    userid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    readonly = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_repository_instances'


class MdlResource(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    tobemigrated = models.SmallIntegerField()
    legacyfiles = models.SmallIntegerField()
    legacyfileslast = models.BigIntegerField(blank=True, null=True)
    display = models.SmallIntegerField()
    displayoptions = models.TextField(blank=True, null=True)
    filterfiles = models.SmallIntegerField()
    revision = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_resource'


class MdlResourceOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=30)
    reference = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    alltext = models.TextField()
    popup = models.TextField()
    options = models.CharField(max_length=255)
    timemodified = models.BigIntegerField()
    oldid = models.BigIntegerField(unique=True)
    cmid = models.BigIntegerField(blank=True, null=True)
    newmodule = models.CharField(max_length=50, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)
    migrated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_resource_old'


class MdlRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    shortname = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    sortorder = models.BigIntegerField(unique=True)
    archetype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mdl_role'


class MdlRoleAllowAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    allowassign = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_role_allow_assign'
        unique_together = (('roleid', 'allowassign'),)


class MdlRoleAllowOverride(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    allowoverride = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_role_allow_override'
        unique_together = (('roleid', 'allowoverride'),)


class MdlRoleAllowSwitch(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    allowswitch = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_role_allow_switch'
        unique_together = (('roleid', 'allowswitch'),)


class MdlRoleAssignments(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    modifierid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    itemid = models.BigIntegerField()
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_role_assignments'


class MdlRoleCapabilities(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    capability = models.CharField(max_length=255)
    permission = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    modifierid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_role_capabilities'
        unique_together = (('roleid', 'contextid', 'capability'),)


class MdlRoleContextLevels(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    contextlevel = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_role_context_levels'
        unique_together = (('contextlevel', 'roleid'),)


class MdlRoleNames(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_role_names'
        unique_together = (('roleid', 'contextid'),)


class MdlRoleSortorder(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    sortoder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_role_sortorder'
        unique_together = (('userid', 'roleid', 'contextid'),)


class MdlScale(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    scale = models.TextField()
    description = models.TextField()
    descriptionformat = models.SmallIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_scale'


class MdlScaleHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    scale = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_scale_history'


class MdlScorm(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    scormtype = models.CharField(max_length=50)
    reference = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    version = models.CharField(max_length=9)
    maxgrade = models.FloatField()
    grademethod = models.SmallIntegerField()
    whatgrade = models.BigIntegerField()
    maxattempt = models.BigIntegerField()
    forcecompleted = models.SmallIntegerField()
    forcenewattempt = models.SmallIntegerField()
    lastattemptlock = models.SmallIntegerField()
    masteryoverride = models.SmallIntegerField()
    displayattemptstatus = models.SmallIntegerField()
    displaycoursestructure = models.SmallIntegerField()
    updatefreq = models.SmallIntegerField()
    sha1hash = models.CharField(max_length=40, blank=True, null=True)
    md5hash = models.CharField(max_length=32)
    revision = models.BigIntegerField()
    launch = models.BigIntegerField()
    skipview = models.SmallIntegerField()
    hidebrowse = models.SmallIntegerField()
    hidetoc = models.SmallIntegerField()
    nav = models.SmallIntegerField()
    navpositionleft = models.BigIntegerField(blank=True, null=True)
    navpositiontop = models.BigIntegerField(blank=True, null=True)
    auto = models.SmallIntegerField()
    popup = models.SmallIntegerField()
    options = models.CharField(max_length=255)
    width = models.BigIntegerField()
    height = models.BigIntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionstatusrequired = models.SmallIntegerField(blank=True, null=True)
    completionscorerequired = models.SmallIntegerField(blank=True, null=True)
    completionstatusallscos = models.SmallIntegerField(blank=True, null=True)
    displayactivityname = models.SmallIntegerField()
    autocommit = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_scorm'


class MdlScormAiccSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    scormid = models.BigIntegerField()
    hacpsession = models.CharField(max_length=255)
    scoid = models.BigIntegerField(blank=True, null=True)
    scormmode = models.CharField(max_length=50, blank=True, null=True)
    scormstatus = models.CharField(max_length=255, blank=True, null=True)
    attempt = models.BigIntegerField(blank=True, null=True)
    lessonstatus = models.CharField(max_length=255, blank=True, null=True)
    sessiontime = models.CharField(max_length=255, blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_scorm_aicc_session'


class MdlScormScoes(models.Model):
    id = models.BigAutoField(primary_key=True)
    scorm = models.BigIntegerField()
    manifest = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    parent = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    launch = models.TextField()
    scormtype = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_scorm_scoes'


class MdlScormScoesData(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_scorm_scoes_data'


class MdlScormScoesTrack(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    scormid = models.BigIntegerField()
    scoid = models.BigIntegerField()
    attempt = models.BigIntegerField()
    element = models.CharField(max_length=255)
    value = models.TextField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_scorm_scoes_track'
        unique_together = (('userid', 'scormid', 'scoid', 'attempt', 'element'),)


class MdlScormSeqMapinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    objectiveid = models.BigIntegerField()
    targetobjectiveid = models.BigIntegerField()
    readsatisfiedstatus = models.SmallIntegerField()
    readnormalizedmeasure = models.SmallIntegerField()
    writesatisfiedstatus = models.SmallIntegerField()
    writenormalizedmeasure = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_mapinfo'
        unique_together = (('scoid', 'id', 'objectiveid'),)


class MdlScormSeqObjective(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    primaryobj = models.SmallIntegerField()
    objectiveid = models.CharField(max_length=255)
    satisfiedbymeasure = models.SmallIntegerField()
    minnormalizedmeasure = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_objective'
        unique_together = (('scoid', 'id'),)


class MdlScormSeqRolluprule(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    childactivityset = models.CharField(max_length=15)
    minimumcount = models.BigIntegerField()
    minimumpercent = models.FloatField()
    conditioncombination = models.CharField(max_length=3)
    action = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_rolluprule'
        unique_together = (('scoid', 'id'),)


class MdlScormSeqRolluprulecond(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    rollupruleid = models.BigIntegerField()
    operator = models.CharField(max_length=5)
    cond = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_rolluprulecond'
        unique_together = (('scoid', 'rollupruleid', 'id'),)


class MdlScormSeqRulecond(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    ruleconditionsid = models.BigIntegerField()
    refrencedobjective = models.CharField(max_length=255)
    measurethreshold = models.FloatField()
    operator = models.CharField(max_length=5)
    cond = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_rulecond'
        unique_together = (('id', 'scoid', 'ruleconditionsid'),)


class MdlScormSeqRuleconds(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    conditioncombination = models.CharField(max_length=3)
    ruletype = models.SmallIntegerField()
    action = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_ruleconds'
        unique_together = (('scoid', 'id'),)


class MdlSessions(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.BigIntegerField()
    sid = models.CharField(unique=True, max_length=128)
    userid = models.BigIntegerField()
    sessdata = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    firstip = models.CharField(max_length=45, blank=True, null=True)
    lastip = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_sessions'


class MdlStatsDaily(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    roleid = models.BigIntegerField()
    stattype = models.CharField(max_length=20)
    stat1 = models.BigIntegerField()
    stat2 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_stats_daily'


class MdlStatsMonthly(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    roleid = models.BigIntegerField()
    stattype = models.CharField(max_length=20)
    stat1 = models.BigIntegerField()
    stat2 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_stats_monthly'


class MdlStatsUserDaily(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    statsreads = models.BigIntegerField()
    statswrites = models.BigIntegerField()
    stattype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mdl_stats_user_daily'


class MdlStatsUserMonthly(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    statsreads = models.BigIntegerField()
    statswrites = models.BigIntegerField()
    stattype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mdl_stats_user_monthly'


class MdlStatsUserWeekly(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    statsreads = models.BigIntegerField()
    statswrites = models.BigIntegerField()
    stattype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mdl_stats_user_weekly'


class MdlStatsWeekly(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    roleid = models.BigIntegerField()
    stattype = models.CharField(max_length=20)
    stat1 = models.BigIntegerField()
    stat2 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_stats_weekly'


class MdlSurvey(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    template = models.BigIntegerField()
    days = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    questions = models.CharField(max_length=255)
    completionsubmit = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_survey'


class MdlSurveyAnalysis(models.Model):
    id = models.BigAutoField(primary_key=True)
    survey = models.BigIntegerField()
    userid = models.BigIntegerField()
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_survey_analysis'


class MdlSurveyAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    survey = models.BigIntegerField()
    question = models.BigIntegerField()
    time = models.BigIntegerField()
    answer1 = models.TextField()
    answer2 = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_survey_answers'


class MdlSurveyQuestions(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=255)
    shorttext = models.CharField(max_length=30)
    multi = models.CharField(max_length=100)
    intro = models.CharField(max_length=50)
    type = models.SmallIntegerField()
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_survey_questions'


class MdlTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    tagcollid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    rawname = models.CharField(max_length=255)
    isstandard = models.SmallIntegerField()
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    flag = models.SmallIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_tag'
        unique_together = (('tagcollid', 'name'),)


class MdlTagArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    component = models.CharField(max_length=100)
    itemtype = models.CharField(max_length=100)
    enabled = models.SmallIntegerField()
    tagcollid = models.BigIntegerField()
    callback = models.CharField(max_length=100, blank=True, null=True)
    callbackfile = models.CharField(max_length=100, blank=True, null=True)
    showstandard = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_tag_area'
        unique_together = (('component', 'itemtype'),)


class MdlTagColl(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    isdefault = models.SmallIntegerField()
    component = models.CharField(max_length=100, blank=True, null=True)
    sortorder = models.IntegerField()
    searchable = models.SmallIntegerField()
    customurl = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_tag_coll'


class MdlTagCorrelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    tagid = models.BigIntegerField()
    correlatedtags = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_tag_correlation'


class MdlTagInstance(models.Model):
    id = models.BigAutoField(primary_key=True)
    tagid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    itemtype = models.CharField(max_length=100)
    itemid = models.BigIntegerField()
    contextid = models.BigIntegerField(blank=True, null=True)
    tiuserid = models.BigIntegerField()
    ordering = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_tag_instance'
        unique_together = (('component', 'itemtype', 'itemid', 'tiuserid', 'tagid'),)


class MdlTaskAdhoc(models.Model):
    id = models.BigAutoField(primary_key=True)
    component = models.CharField(max_length=255)
    classname = models.CharField(max_length=255)
    nextruntime = models.BigIntegerField()
    faildelay = models.BigIntegerField(blank=True, null=True)
    customdata = models.TextField(blank=True, null=True)
    blocking = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_task_adhoc'


class MdlTaskScheduled(models.Model):
    id = models.BigAutoField(primary_key=True)
    component = models.CharField(max_length=255)
    classname = models.CharField(unique=True, max_length=255)
    lastruntime = models.BigIntegerField(blank=True, null=True)
    nextruntime = models.BigIntegerField(blank=True, null=True)
    blocking = models.SmallIntegerField()
    minute = models.CharField(max_length=25)
    hour = models.CharField(max_length=25)
    day = models.CharField(max_length=25)
    month = models.CharField(max_length=25)
    dayofweek = models.CharField(max_length=25)
    faildelay = models.BigIntegerField(blank=True, null=True)
    customised = models.SmallIntegerField()
    disabled = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_task_scheduled'


class MdlToolCohortroles(models.Model):
    id = models.BigAutoField(primary_key=True)
    cohortid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_tool_cohortroles'
        unique_together = (('cohortid', 'roleid', 'userid'),)


class MdlToolCustomlang(models.Model):
    id = models.BigAutoField(primary_key=True)
    lang = models.CharField(max_length=20)
    componentid = models.BigIntegerField()
    stringid = models.CharField(max_length=255)
    original = models.TextField()
    master = models.TextField(blank=True, null=True)
    local = models.TextField(blank=True, null=True)
    timemodified = models.BigIntegerField()
    timecustomized = models.BigIntegerField(blank=True, null=True)
    outdated = models.SmallIntegerField(blank=True, null=True)
    modified = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_tool_customlang'
        unique_together = (('lang', 'componentid', 'stringid'),)


class MdlToolCustomlangComponents(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_tool_customlang_components'


class MdlToolMonitorEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    eventname = models.CharField(max_length=254)
    contextid = models.BigIntegerField()
    contextlevel = models.BigIntegerField()
    contextinstanceid = models.BigIntegerField()
    link = models.CharField(max_length=254)
    courseid = models.BigIntegerField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_tool_monitor_events'


class MdlToolMonitorHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    sid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timesent = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_tool_monitor_history'
        unique_together = (('sid', 'userid', 'timesent'),)


class MdlToolMonitorRules(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    name = models.CharField(max_length=254)
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    plugin = models.CharField(max_length=254)
    eventname = models.CharField(max_length=254)
    template = models.TextField()
    templateformat = models.SmallIntegerField()
    frequency = models.SmallIntegerField()
    timewindow = models.IntegerField()
    timemodified = models.BigIntegerField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_tool_monitor_rules'


class MdlToolMonitorSubscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    ruleid = models.BigIntegerField()
    cmid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    lastnotificationsent = models.BigIntegerField()
    inactivedate = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_tool_monitor_subscriptions'


class MdlToolRecyclebinCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    categoryid = models.BigIntegerField()
    shortname = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_tool_recyclebin_category'


class MdlToolRecyclebinCourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    section = models.BigIntegerField()
    module = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_tool_recyclebin_course'


class MdlToolUsertoursSteps(models.Model):
    id = models.BigAutoField(primary_key=True)
    tourid = models.BigIntegerField()
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    targettype = models.SmallIntegerField()
    targetvalue = models.TextField()
    sortorder = models.BigIntegerField()
    configdata = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_tool_usertours_steps'


class MdlToolUsertoursTours(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    pathmatch = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.SmallIntegerField()
    sortorder = models.BigIntegerField()
    configdata = models.TextField()

    class Meta:
        managed = False
        db_table = 'mdl_tool_usertours_tours'


class MdlUpgradeLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.BigIntegerField()
    plugin = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    targetversion = models.CharField(max_length=100, blank=True, null=True)
    info = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    backtrace = models.TextField(blank=True, null=True)
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_upgrade_log'


class MdlUrl(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    externalurl = models.TextField()
    display = models.SmallIntegerField()
    displayoptions = models.TextField(blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_url'


class MdlUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    auth = models.CharField(max_length=20)
    confirmed = models.SmallIntegerField()
    policyagreed = models.SmallIntegerField()
    deleted = models.SmallIntegerField()
    suspended = models.SmallIntegerField()
    mnethostid = models.BigIntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    emailstop = models.SmallIntegerField()
    icq = models.CharField(max_length=15)
    skype = models.CharField(max_length=50)
    yahoo = models.CharField(max_length=50)
    aim = models.CharField(max_length=50)
    msn = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    institution = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=2)
    lang = models.CharField(max_length=30)
    calendartype = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timezone = models.CharField(max_length=100)
    firstaccess = models.BigIntegerField()
    lastaccess = models.BigIntegerField()
    lastlogin = models.BigIntegerField()
    currentlogin = models.BigIntegerField()
    lastip = models.CharField(max_length=45)
    secret = models.CharField(max_length=15)
    picture = models.BigIntegerField()
    url = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    mailformat = models.SmallIntegerField()
    maildigest = models.SmallIntegerField()
    maildisplay = models.SmallIntegerField()
    autosubscribe = models.SmallIntegerField()
    trackforums = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    trustbitmask = models.BigIntegerField()
    imagealt = models.CharField(max_length=255, blank=True, null=True)
    lastnamephonetic = models.CharField(max_length=255, blank=True, null=True)
    firstnamephonetic = models.CharField(max_length=255, blank=True, null=True)
    middlename = models.CharField(max_length=255, blank=True, null=True)
    alternatename = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_user'
        unique_together = (('mnethostid', 'username'),)


class MdlUserDevices(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    appid = models.CharField(max_length=128)
    name = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    platform = models.CharField(max_length=32)
    version = models.CharField(max_length=32)
    pushid = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_user_devices'
        unique_together = (('pushid', 'userid'),)


class MdlUserEnrolments(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.BigIntegerField()
    enrolid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    modifierid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_user_enrolments'
        unique_together = (('enrolid', 'userid'),)


class MdlUserInfoCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_user_info_category'


class MdlUserInfoData(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    fieldid = models.BigIntegerField()
    data = models.TextField()
    dataformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_user_info_data'
        unique_together = (('userid', 'fieldid'),)


class MdlUserInfoField(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(max_length=255)
    name = models.TextField()
    datatype = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField()
    categoryid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    required = models.SmallIntegerField()
    locked = models.SmallIntegerField()
    visible = models.SmallIntegerField()
    forceunique = models.SmallIntegerField()
    signup = models.SmallIntegerField()
    defaultdata = models.TextField(blank=True, null=True)
    defaultdataformat = models.SmallIntegerField()
    param1 = models.TextField(blank=True, null=True)
    param2 = models.TextField(blank=True, null=True)
    param3 = models.TextField(blank=True, null=True)
    param4 = models.TextField(blank=True, null=True)
    param5 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_user_info_field'


class MdlUserLastaccess(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    timeaccess = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_user_lastaccess'
        unique_together = (('userid', 'courseid'),)


class MdlUserPasswordHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    hash = models.CharField(max_length=255)
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_user_password_history'


class MdlUserPasswordResets(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    timerequested = models.BigIntegerField()
    timererequested = models.BigIntegerField()
    token = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'mdl_user_password_resets'


class MdlUserPreferences(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=1333)

    class Meta:
        managed = False
        db_table = 'mdl_user_preferences'
        unique_together = (('userid', 'name'),)


class MdlUserPrivateKey(models.Model):
    id = models.BigAutoField(primary_key=True)
    script = models.CharField(max_length=128)
    value = models.CharField(max_length=128)
    userid = models.BigIntegerField()
    instance = models.BigIntegerField(blank=True, null=True)
    iprestriction = models.CharField(max_length=255, blank=True, null=True)
    validuntil = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_user_private_key'


class MdlWiki(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    firstpagetitle = models.CharField(max_length=255)
    wikimode = models.CharField(max_length=20)
    defaultformat = models.CharField(max_length=20)
    forceformat = models.SmallIntegerField()
    editbegin = models.BigIntegerField()
    editend = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_wiki'


class MdlWikiLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    subwikiid = models.BigIntegerField()
    frompageid = models.BigIntegerField()
    topageid = models.BigIntegerField()
    tomissingpage = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_wiki_links'


class MdlWikiLocks(models.Model):
    id = models.BigAutoField(primary_key=True)
    pageid = models.BigIntegerField()
    sectionname = models.CharField(max_length=255, blank=True, null=True)
    userid = models.BigIntegerField()
    lockedat = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_wiki_locks'


class MdlWikiPages(models.Model):
    id = models.BigAutoField(primary_key=True)
    subwikiid = models.BigIntegerField()
    title = models.CharField(max_length=255)
    cachedcontent = models.TextField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    timerendered = models.BigIntegerField()
    userid = models.BigIntegerField()
    pageviews = models.BigIntegerField()
    readonly = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_wiki_pages'
        unique_together = (('subwikiid', 'title', 'userid'),)


class MdlWikiSubwikis(models.Model):
    id = models.BigAutoField(primary_key=True)
    wikiid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_wiki_subwikis'
        unique_together = (('wikiid', 'groupid', 'userid'),)


class MdlWikiSynonyms(models.Model):
    id = models.BigAutoField(primary_key=True)
    subwikiid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    pagesynonym = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mdl_wiki_synonyms'
        unique_together = (('pageid', 'pagesynonym'),)


class MdlWikiVersions(models.Model):
    id = models.BigAutoField(primary_key=True)
    pageid = models.BigIntegerField()
    content = models.TextField()
    contentformat = models.CharField(max_length=20)
    version = models.IntegerField()
    timecreated = models.BigIntegerField()
    userid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_wiki_versions'


class MdlWorkshop(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    instructauthors = models.TextField(blank=True, null=True)
    instructauthorsformat = models.SmallIntegerField()
    instructreviewers = models.TextField(blank=True, null=True)
    instructreviewersformat = models.SmallIntegerField()
    timemodified = models.BigIntegerField()
    phase = models.SmallIntegerField(blank=True, null=True)
    useexamples = models.SmallIntegerField(blank=True, null=True)
    usepeerassessment = models.SmallIntegerField(blank=True, null=True)
    useselfassessment = models.SmallIntegerField(blank=True, null=True)
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    strategy = models.CharField(max_length=30)
    evaluation = models.CharField(max_length=30)
    gradedecimals = models.SmallIntegerField(blank=True, null=True)
    nattachments = models.SmallIntegerField(blank=True, null=True)
    submissionfiletypes = models.CharField(max_length=255, blank=True, null=True)
    latesubmissions = models.SmallIntegerField(blank=True, null=True)
    maxbytes = models.BigIntegerField(blank=True, null=True)
    examplesmode = models.SmallIntegerField(blank=True, null=True)
    submissionstart = models.BigIntegerField(blank=True, null=True)
    submissionend = models.BigIntegerField(blank=True, null=True)
    assessmentstart = models.BigIntegerField(blank=True, null=True)
    assessmentend = models.BigIntegerField(blank=True, null=True)
    phaseswitchassessment = models.SmallIntegerField()
    conclusion = models.TextField(blank=True, null=True)
    conclusionformat = models.SmallIntegerField()
    overallfeedbackmode = models.SmallIntegerField(blank=True, null=True)
    overallfeedbackfiles = models.SmallIntegerField(blank=True, null=True)
    overallfeedbackfiletypes = models.CharField(max_length=255, blank=True, null=True)
    overallfeedbackmaxbytes = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop'


class MdlWorkshopAggregations(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    userid = models.BigIntegerField()
    gradinggrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    timegraded = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop_aggregations'
        unique_together = (('workshopid', 'userid'),)


class MdlWorkshopAssessments(models.Model):
    id = models.BigAutoField(primary_key=True)
    submissionid = models.BigIntegerField()
    reviewerid = models.BigIntegerField()
    weight = models.BigIntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggradeover = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggradeoverby = models.BigIntegerField(blank=True, null=True)
    feedbackauthor = models.TextField(blank=True, null=True)
    feedbackauthorformat = models.SmallIntegerField(blank=True, null=True)
    feedbackauthorattachment = models.SmallIntegerField(blank=True, null=True)
    feedbackreviewer = models.TextField(blank=True, null=True)
    feedbackreviewerformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop_assessments'


class MdlWorkshopAssessmentsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    submissionid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timegraded = models.BigIntegerField()
    timeagreed = models.BigIntegerField()
    grade = models.FloatField()
    gradinggrade = models.SmallIntegerField()
    teachergraded = models.SmallIntegerField()
    mailed = models.SmallIntegerField()
    resubmission = models.SmallIntegerField()
    donotuse = models.SmallIntegerField()
    generalcomment = models.TextField(blank=True, null=True)
    teachercomment = models.TextField(blank=True, null=True)
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop_assessments_old'


class MdlWorkshopCommentsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    assessmentid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    mailed = models.SmallIntegerField()
    comments = models.TextField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop_comments_old'


class MdlWorkshopElementsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    elementno = models.SmallIntegerField()
    description = models.TextField()
    scale = models.SmallIntegerField()
    maxscore = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    stddev = models.FloatField()
    totalassessments = models.BigIntegerField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop_elements_old'


class MdlWorkshopGrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    assessmentid = models.BigIntegerField()
    strategy = models.CharField(max_length=30)
    dimensionid = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    peercomment = models.TextField(blank=True, null=True)
    peercommentformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop_grades'
        unique_together = (('assessmentid', 'strategy', 'dimensionid'),)


class MdlWorkshopGradesOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    assessmentid = models.BigIntegerField()
    elementno = models.BigIntegerField()
    feedback = models.TextField()
    grade = models.SmallIntegerField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop_grades_old'


class MdlWorkshopOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    wtype = models.SmallIntegerField()
    nelements = models.SmallIntegerField()
    nattachments = models.SmallIntegerField()
    phase = models.SmallIntegerField()
    format = models.SmallIntegerField()
    gradingstrategy = models.SmallIntegerField()
    resubmit = models.SmallIntegerField()
    agreeassessments = models.SmallIntegerField()
    hidegrades = models.SmallIntegerField()
    anonymous = models.SmallIntegerField()
    includeself = models.SmallIntegerField()
    maxbytes = models.BigIntegerField()
    submissionstart = models.BigIntegerField()
    assessmentstart = models.BigIntegerField()
    submissionend = models.BigIntegerField()
    assessmentend = models.BigIntegerField()
    releasegrades = models.BigIntegerField()
    grade = models.SmallIntegerField()
    gradinggrade = models.SmallIntegerField()
    ntassessments = models.SmallIntegerField()
    assessmentcomps = models.SmallIntegerField()
    nsassessments = models.SmallIntegerField()
    overallocation = models.SmallIntegerField()
    timemodified = models.BigIntegerField()
    teacherweight = models.SmallIntegerField()
    showleaguetable = models.SmallIntegerField()
    usepassword = models.SmallIntegerField()
    password = models.CharField(max_length=32)
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop_old'


class MdlWorkshopRubricsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    elementno = models.BigIntegerField()
    rubricno = models.SmallIntegerField()
    description = models.TextField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop_rubrics_old'


class MdlWorkshopStockcommentsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    elementno = models.BigIntegerField()
    comments = models.TextField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop_stockcomments_old'


class MdlWorkshopSubmissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    example = models.SmallIntegerField(blank=True, null=True)
    authorid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    contentformat = models.SmallIntegerField()
    contenttrust = models.SmallIntegerField()
    attachment = models.SmallIntegerField(blank=True, null=True)
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradeover = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradeoverby = models.BigIntegerField(blank=True, null=True)
    feedbackauthor = models.TextField(blank=True, null=True)
    feedbackauthorformat = models.SmallIntegerField(blank=True, null=True)
    timegraded = models.BigIntegerField(blank=True, null=True)
    published = models.SmallIntegerField(blank=True, null=True)
    late = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_workshop_submissions'


class MdlWorkshopSubmissionsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    userid = models.BigIntegerField()
    title = models.CharField(max_length=100)
    timecreated = models.BigIntegerField()
    mailed = models.SmallIntegerField()
    description = models.TextField()
    gradinggrade = models.SmallIntegerField()
    finalgrade = models.SmallIntegerField()
    late = models.SmallIntegerField()
    nassessments = models.BigIntegerField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshop_submissions_old'


class MdlWorkshopallocationScheduled(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField(unique=True)
    enabled = models.SmallIntegerField()
    submissionend = models.BigIntegerField()
    timeallocated = models.BigIntegerField(blank=True, null=True)
    settings = models.TextField(blank=True, null=True)
    resultstatus = models.BigIntegerField(blank=True, null=True)
    resultmessage = models.CharField(max_length=1333, blank=True, null=True)
    resultlog = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshopallocation_scheduled'


class MdlWorkshopevalBestSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField(unique=True)
    comparison = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshopeval_best_settings'


class MdlWorkshopformAccumulative(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)
    grade = models.BigIntegerField()
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshopform_accumulative'


class MdlWorkshopformComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshopform_comments'


class MdlWorkshopformNumerrors(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)
    descriptiontrust = models.BigIntegerField(blank=True, null=True)
    grade0 = models.CharField(max_length=50, blank=True, null=True)
    grade1 = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshopform_numerrors'


class MdlWorkshopformNumerrorsMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    nonegative = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'mdl_workshopform_numerrors_map'
        unique_together = (('workshopid', 'nonegative'),)


class MdlWorkshopformRubric(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshopform_rubric'


class MdlWorkshopformRubricConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField(unique=True)
    layout = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshopform_rubric_config'


class MdlWorkshopformRubricLevels(models.Model):
    id = models.BigAutoField(primary_key=True)
    dimensionid = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    definition = models.TextField(blank=True, null=True)
    definitionformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_workshopform_rubric_levels'
